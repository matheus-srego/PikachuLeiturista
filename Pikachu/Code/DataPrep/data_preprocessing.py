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
        # Criando índice temporal dos dados..=
        initial_date = time.strftime( CONSTANTS.FORMAT_DATE_EUA, time.localtime( int( dataframe.loc[0, CONSTANTS.COLUMN_TIME] ) ) )
        index = pd.date_range( initial_date, periods=len( dataframe ), freq='min' )
        
        # Criando índice temporal e agrupando linhas por dia..
        dataframe = dataframe.set_index( pd.DatetimeIndex( data=index, name=CONSTANTS.INDEX_DATETIME ) ).groupby( pd.Grouper( freq='D' ) ).mean()
        
        return dataframe
    
    def rename_columms( self, dataframe ):
        # Somando consumo de energia de todas as cozinhas..
        dataframe[CONSTANTS.KW_KITCHEN] = dataframe[CONSTANTS.COLUMN_KITCHEN_12] + dataframe[CONSTANTS.COLUMN_KITCHEN_14] + dataframe[CONSTANTS.COLUMN_KITCHEN_38]
        
        dataframe.rename( 
            columns = {
                CONSTANTS.COLUMN_TEMPERATURE: CONSTANTS.C_TEMPERATURE,
                CONSTANTS.COLUMN_USE: CONSTANTS.KW_USE,
                CONSTANTS.COLUMN_HOME_OFFICE: CONSTANTS.KW_HOME_OFFICE,
                CONSTANTS.COLUMN_LIVING_ROOM: CONSTANTS.KW_LIVING_ROOM,
                CONSTANTS.COLUMN_WINE_CELLAR: CONSTANTS.KW_WINE_CELLAR,
                CONSTANTS.COLUMN_GARAGE_DOOR: CONSTANTS.KW_GARAGE_DOOR,
                CONSTANTS.COLUMN_BARN: CONSTANTS.KW_BARN
            }, 
            inplace=True 
        )
        
        print( dataframe )
        
        return dataframe
    
    def clean_dataframe( self, dataframe ):
        # Removendo Nan e Null..
        dataframe = dataframe.dropna()
        
        del dataframe[CONSTANTS.COLUMN_HOUSE_OVERALL]
        del dataframe[CONSTANTS.COLUMN_APPARENT_TEMPERATURE]
        del dataframe[CONSTANTS.COLUMN_SOLAR]
        del dataframe[CONSTANTS.COLUMN_HUMIDITY]
        del dataframe[CONSTANTS.COLUMN_VISIBILITY]
        del dataframe[CONSTANTS.COLUMN_PRESSURE]
        del dataframe[CONSTANTS.COLUMN_WIND_SPEED]
        del dataframe[CONSTANTS.COLUMN_WIND_BEARING]
        del dataframe[CONSTANTS.COLUMN_PRECIP_INTENSITY]
        del dataframe[CONSTANTS.COLUMN_DEW_POINT]
        del dataframe[CONSTANTS.COLUMN_PRECIP_PROBABILITY]
        del dataframe[CONSTANTS.COLUMN_GEN]
        del dataframe[CONSTANTS.COLUMN_DISHWASHER]
        del dataframe[CONSTANTS.COLUMN_FURNACE_1]
        del dataframe[CONSTANTS.COLUMN_FURNACE_2]
        del dataframe[CONSTANTS.COLUMN_FRIDGE]
        del dataframe[CONSTANTS.COLUMN_WELL]
        del dataframe[CONSTANTS.COLUMN_MICROWAVE]
        del dataframe[CONSTANTS.COLUMN_KITCHEN_12]
        del dataframe[CONSTANTS.COLUMN_KITCHEN_14]
        del dataframe[CONSTANTS.COLUMN_KITCHEN_38]
        
        return dataframe
    
    def organizing_dataframe( self, dataframe ):
        # Reposicionando colunas..
        dataframe = dataframe[['dataframe','C_temperature', 'KW_use', 'KW_kitchen', 'KW_living_room', 'KW_home_office', 'KW_wine_cellar', 'KW_barn', 'KW_garage_door']]
        
        return dataframe
        
    def start_formatting_CSV( self ):
        DataPreprocessing.__init__( self )
        
        path_raw_csv = self.CONSTANTS.PATH_RAW_CSV
        
        dataframe = DataPreprocessing.read_csv( self, path_raw_csv )
        dataframe = DataPreprocessing.rename_columms( self, dataframe )
        dataframe = DataPreprocessing.processing( self, dataframe )
        dataframe = DataPreprocessing.clean_dataframe( self, dataframe )
        # dataframe = DataPreprocessing.organizing_dataframe( self, dataframe )
        
        print( dataframe )

        DataPreprocessing.create_csv( self, dataframe )
        