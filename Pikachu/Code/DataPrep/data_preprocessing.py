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
        
    # 1
    def read_csv( self, csv ):
        dataframe = pd.read_csv( csv, low_memory=False )
        
        return dataframe
        
    # 2
    def processing( self, dataframe ):
        # Criando índice temporal dos dados..
        format_date = self.CONSTANTS.FORMAT_DATE_EUA

        initial_date = time.strftime( format_date, time.localtime( int( dataframe.loc[0, self.CONSTANTS.COLUMN_TIME] ) ) )
        index = pd.date_range( initial_date, periods=len( dataframe ), freq='min' )
        
        dataframe = dataframe.set_index( pd.DatetimeIndex( index ) )
        
        return dataframe

    # 3
    def create_new_columns( self, dataframe ):
        # Mudando nome das colunas..
        dataframe[self.CONSTANTS.APPARENT_TEMPERATURE] = dataframe[self.CONSTANTS.COLUMN_APPARENT_TEMPERATURE]
        dataframe[self.CONSTANTS.KW_USE] = dataframe[self.CONSTANTS.COLUMN_USE]
        dataframe[self.CONSTANTS.KW_GENERATION] = dataframe[self.CONSTANTS.COLUMN_GEN]
        dataframe[self.CONSTANTS.KW_HOUSE] = dataframe[self.CONSTANTS.COLUMN_HOUSE_OVERALL]
        dataframe[self.CONSTANTS.KW_HOME_OFFICE] = dataframe[self.CONSTANTS.COLUMN_HOME_OFFICE]
        dataframe[self.CONSTANTS.KW_LIVING_ROOM] = dataframe[self.CONSTANTS.COLUMN_LIVING_ROOM]
        dataframe[self.CONSTANTS.KW_KITCHEN] = dataframe[self.CONSTANTS.COLUMN_KITCHEN_12] + dataframe[self.CONSTANTS.COLUMN_KITCHEN_14] + dataframe[self.CONSTANTS.COLUMN_KITCHEN_38]
        dataframe[self.CONSTANTS.KW_WINE_CELLAR] = dataframe[self.CONSTANTS.COLUMN_WINE_CELLAR]
        dataframe[self.CONSTANTS.KW_GARAGE_DOOR] = dataframe[self.CONSTANTS.COLUMN_GARAGE_DOOR]
        dataframe[self.CONSTANTS.KW_BARN] = dataframe[self.CONSTANTS.COLUMN_BARN]

        return dataframe

    # 4
    def remove_columns( self, dataframe ):
        dataframe = dataframe.dropna()
        
        # Removendo colunas que não serão utilizadas..
        del dataframe[self.CONSTANTS.COLUMNS_SOLAR]
        del dataframe[self.CONSTANTS.COLUMN_ICON]
        del dataframe[self.CONSTANTS.COLUMN_HUMIDITY]
        del dataframe[self.CONSTANTS.COLUMN_VISIBILITY]
        del dataframe[self.CONSTANTS.COLUMN_SUMARY]
        del dataframe[self.CONSTANTS.COLUMN_PRESSURE]
        del dataframe[self.CONSTANTS.COLUMN_WIND_SPEED]
        del dataframe[self.CONSTANTS.COLUMN_CLOUD_COVER]
        del dataframe[self.CONSTANTS.COLUMN_WIND_BEARING]
        del dataframe[self.CONSTANTS.COLUMN_PRECIP_INTENSITY]
        del dataframe[self.CONSTANTS.COLUMN_DEW_POINT]
        del dataframe[self.CONSTANTS.COLUMN_PRECIP_PROBABILITY]
        
        # Removendo colunas de eletrodomésticos..
        del dataframe[self.CONSTANTS.COLUMN_DISHWASHER]
        del dataframe[self.CONSTANTS.COLUMN_FURNACE_1]
        del dataframe[self.CONSTANTS.COLUMN_FURNACE_2]
        del dataframe[self.CONSTANTS.COLUMN_FRIDGE]
        del dataframe[self.CONSTANTS.COLUMN_WELL]
        del dataframe[self.CONSTANTS.COLUMN_MICROWAVE]
        
        # Deletando colunas com nomes antigos..
        del dataframe[self.CONSTANTS.COLUMN_APPARENT_TEMPERATURE]
        del dataframe[self.CONSTANTS.COLUMN_USE]
        del dataframe[self.CONSTANTS.COLUMN_GEN]
        del dataframe[self.CONSTANTS.COLUMN_HOUSE_OVERALL]
        del dataframe[self.CONSTANTS.COLUMN_HOME_OFFICE]
        del dataframe[self.CONSTANTS.COLUMN_LIVING_ROOM]
        del dataframe[self.CONSTANTS.COLUMN_KITCHEN_12]
        del dataframe[self.CONSTANTS.COLUMN_KITCHEN_14]
        del dataframe[self.CONSTANTS.COLUMN_KITCHEN_38]
        del dataframe[self.CONSTANTS.COLUMN_WINE_CELLAR]
        del dataframe[self.CONSTANTS.COLUMN_GARAGE_DOOR]
        del dataframe[self.CONSTANTS.COLUMN_BARN]

        del dataframe[self.CONSTANTS.COLUMN_TIME]
        
        return dataframe
        
    # 5
    def create_csv( self, dataframe ):
        dataframe.to_csv( self.CONSTANTS.PATH_PROCESSED_CSV, index=True, header=True )
    
    # 0
    # def hasFileOrNeedDownload( self ):
    #     if( os.path.exists( self.CONSTANTS.PATH_RAW_CSV ) == False and os.path.exists( self.CONSTANTS.PATH_PROCESSED_CSV ) == False ):
    #         Download.csv( self.CONSTANTS.URL_CSV, self.CONSTANTS.PATH_RAW_CSV )
    #         return True
    #     return False
        
    def start_formatting_CSV( self ):
        DataPreprocessing.__init__( self )

        # needProcess = DataPreprocessing.hasFileOrNeedDownload( self )

        # if( needProcess == True ):
        path_raw_csv = self.CONSTANTS.PATH_RAW_CSV
        dataframe = DataPreprocessing.read_csv( self, path_raw_csv )
        # dataframe = DataPreprocessing.processing( self, dataframe )
        # dataframe = DataPreprocessing.create_new_columns( self, dataframe )
        # dataframe = DataPreprocessing.remove_columns( self, dataframe )

        print( dataframe )

        # DataPreprocessing.create_csv( self, dataframe )
        