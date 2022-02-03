from DataPrep.data_preprocessing import DataPreprocessing

class MiauInitalizer:
    
    def __init__( self ):
        print( 'Inicializando M.I.A.U.' )

    def main( self ):
        DataPreprocessing.start_formatting_CSV( self )
        
if __name__ == '__main__':
    miau = MiauInitalizer()
    miau.main()
    
    