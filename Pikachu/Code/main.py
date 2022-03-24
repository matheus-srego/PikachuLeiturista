from DataPrep.data_preprocessing import DataPreprocessing

class PikachuInitalizer:
    
    def __init__( self ):
        print( 'Inicializando Pikachu Leiturista' )

    def main( self ):
        DataPreprocessing.start_formatting_CSV( self )
        
if __name__ == '__main__':
    initializer = PikachuInitalizer()
    initializer.main()
    