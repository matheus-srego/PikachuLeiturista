import pandas as pd
import time
import os

# from DataPrep.download import Download
import Shared.CONSTANTS as CONSTANTS

class DataPreprocessing( object ):
    
    def __init__( self ):
        self.CONSTANTS = CONSTANTS
        self.PATH_RAW_CSV = CONSTANTS.PATH_RAW_CSV
        self.PATH_PROCESSED_CSV = CONSTANTS.PATH_PROCESSED_CSV
    
    def read_csv( self, csv ):
        dataframe = pd.read_csv( csv, low_memory=False )
        
        return dataframe
    
    def create_csv( self, dataframe ):
        dataframe.to_csv( self.CONSTANTS.PATH_PROCESSED_CSV, index=True, header=True )
    
    def processing( self, dataframe ):
        # Somando consumo de energia de todas as cozinhas..
        dataframe['KW_kitchen'] = dataframe['Kitchen 12 [kW]'] + dataframe['Kitchen 14 [kW]'] + dataframe['Kitchen 38 [kW]']
        
        # Criando índice temporal dos dados..
        format_date = '%Y-%m-%d %H:%M:%S'
        
        initial_date = time.strftime( format_date, time.localtime( int( dataframe.loc[0, 'time'] ) ) )
        index = pd.date_range( initial_date, periods=len( dataframe ), freq='min' )
        
        # Criando índice temporal e agrupando por dia..
        dataframe = dataframe.set_index( pd.DatetimeIndex( data=index, name='datetime' ) ).groupby( pd.Grouper( freq='D' ) ).mean()
        
        return dataframe
    
    def rename_columms( self, dataframe ):
        dataframe.rename( columns={
              'temperature': 'C_temperature',
              'use [kW]': 'KW_use',
              'Home office [kW]': 'KW_home_office',
              'Living room [kW]': 'KW_living_room',
              'Wine cellar [kW]': 'KW_wine_cellar',
              'Garage door [kW]': 'KW_garage_door',
              'Barn [kW]': 'KW_barn'
            }, 
            inplace=True 
        )
        
        return dataframe
    
    def clean_dataframe( self, dataframe ):
        # Removendo Nan e Null..
        dataframe = dataframe.dropna()
        
        # Removendo colunas que não serão utilizadas..
        # del dataframe['time']
        del dataframe['House overall [kW]']
        del dataframe['apparentTemperature']
        del dataframe['Solar [kW]']
        # del dataframe['icon']
        del dataframe['humidity']
        del dataframe['visibility']
        # del dataframe['summary']
        del dataframe['pressure']
        del dataframe['windSpeed']
        # del dataframe['cloudCover']
        del dataframe['windBearing']
        del dataframe['precipIntensity']
        del dataframe['dewPoint']
        del dataframe['precipProbability']
        
        # Removendo colunas de eletrodomésticos..
        del dataframe['gen [kW]']
        del dataframe['Dishwasher [kW]']
        del dataframe['Furnace 1 [kW]']
        del dataframe['Furnace 2 [kW]']
        del dataframe['Fridge [kW]']
        del dataframe['Well [kW]']
        del dataframe['Microwave [kW]']
        
        # Deletando colunas com nomes antigos..
        del dataframe['Kitchen 12 [kW]']
        del dataframe['Kitchen 14 [kW]']
        del dataframe['Kitchen 38 [kW]']
        
        return dataframe
    
    def organizing_dataframe( self, dataframe ):
        # Reposicionando colunas..
        dataframe = dataframe[['C_temperature', 'KW_use', 'KW_kitchen', 'KW_living_room', 'KW_home_office', 'KW_wine_cellar', 'KW_barn', 'KW_garage_door']]
        
        return dataframe
        
    def start_formatting_CSV( self ):
        DataPreprocessing.__init__( self )
        
        path_raw_csv = self.CONSTANTS.PATH_RAW_CSV
        dataframe = DataPreprocessing.read_csv( self, path_raw_csv )
        dataframe = DataPreprocessing.rename_columms( self, dataframe )
        dataframe = DataPreprocessing.processing( self, dataframe )
        dataframe = DataPreprocessing.clean_dataframe( self, dataframe )
        dataframe = DataPreprocessing.organizing_dataframe( self, dataframe )
        
        print( dataframe )

        DataPreprocessing.create_csv( self, dataframe )
        