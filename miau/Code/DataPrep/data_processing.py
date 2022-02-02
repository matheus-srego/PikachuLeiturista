import pandas as pd
import time

class DataProcessing( object ):
    
    def __init__( self, CSV_BASE='~/environment/M.I.A.U./HomeC.csv', NEW_CSV='~/environment/M.I.A.U./miau/Data/Processed/home.csv' ):
        self.CSV_BASE = CSV_BASE #'/M.I.A.U./HomeC.csv'
        self.NEW_CSV = NEW_CSV #'~/miau/Data/Processed/home.csv'
        
    # 1
    def read_csv( self, csv ):
        dataframe = pd.read_csv( csv )
        
        print( dataframe )
        
        return dataframe
        
    # 4
    def create_csv( self, dataframe ):
        dataframe.to_csv( self.NEW_CSV, index=True, header=True )
        
    # 3
    def processing( self, dataframe ):
        # Criando índice temporal dos dados..
        format_date = '%Y-%m-%d %H:%M:%S'
        initial_date = time.strftime( format_date, time.localtime( int( dataframe.loc[0, 'time'] ) ) )
        index = pd.date_range( initial_date, periods=len( dataframe ), freq='min' )
        
        dataframe = dataframe.set_index( pd.DatetimeIndex( index ) )
        
        # Mudando nome das colunas..
        dataframe['apparent_temperature'] = dataframe['apparentTemperature']
        dataframe['KW_use'] = dataframe['use [kW]']
        dataframe['KW_generation'] = dataframe['gen [kW]']
        dataframe['KW_house'] = dataframe['House overall [kW]']
        dataframe['KW_home_office'] = dataframe['Home office [kW]']
        dataframe['KW_living_room'] = dataframe['Living room [kW]']
        dataframe['KW_kitchen'] = dataframe['Kitchen 12 [kW]'] + dataframe['Kitchen 14 [kW]'] + dataframe['Kitchen 38 [kW]']
        dataframe['KW_wine_cellar'] = dataframe['Wine cellar [kW]']
        dataframe['KW_garage_door'] = dataframe['Garage door [kW]']
        dataframe['KW_barn'] = dataframe['Barn [kW]']
        
        return dataframe
        
    # 2
    def remove_columns( self, dataframe ):
        dataframe = dataframe.dropna()
        
        # Removendo colunas que não serão utilizadas..
        del dataframe['Solar [kW]']
        del dataframe['icon']
        del dataframe['humidity']
        del dataframe['visibility']
        del dataframe['summary']
        del dataframe['pressure']
        del dataframe['windSpeed']
        del dataframe['cloudCover']
        del dataframe['windBearing']
        del dataframe['precipIntensity']
        del dataframe['dewPoint']
        del dataframe['precipProbability']
        
        # Removendo colunas de eletrodomésticos..
        del dataframe['Dishwasher [kW]']
        del dataframe['Furnace 1 [kW]']
        del dataframe['Furnace 2 [kW]']
        del dataframe['Fridge [kW]']
        del dataframe['Well [kW]']
        del dataframe['Microwave [kW]']
        
        # Deletando colunas com nomes antigos..
        del dataframe['apparentTemperature']
        del dataframe['use [kW]']
        del dataframe['gen [kW]']
        del dataframe['House overall [kW]']
        del dataframe['Home office [kW]']
        del dataframe['Living room [kW]']
        del dataframe['Kitchen 12 [kW]']
        del dataframe['Kitchen 14 [kW]']
        del dataframe['Kitchen 38 [kW]']
        del dataframe['Wine cellar [kW]']
        del dataframe['Garage door [kW]']
        del dataframe['Barn [kW]']
        
        del dataframe['time']
        
        return dataframe
        
    def start_formatting_CSV( self ):
        DataProcessing.__init__( self )
        
        dataframe = DataProcessing.read_csv( self, self.CSV_BASE )
        dataframe = DataProcessing.processing( self, dataframe )
        
        dataframe = DataProcessing.remove_columns( self, dataframe )
        DataProcessing.create_csv( self, dataframe )
        