# import os.path
from DataPrep.data_processing import DataProcessing

class Miau:
    
    def __init__( self ):
        print( 'Inicializando MIAU' )

    def main( self ):
        DataProcessing.start_formatting_CSV( self )
        
if __name__ == '__main__':
    miau = Miau()
    miau.main()
        # if( os.path.exists( '~/miau/Data/Processed/home.csv' ) ):
            # print( 'Não há necessidade de limpar o CSV, o mesmo já está gerado!' )
        # else:
    
    