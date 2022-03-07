import requests

class Download( object ):

    def csv( url, path ):
        response = requests.get( url, stream=True )

        if( response.status_code == requests.codes.OK ):
            with( open( path, 'wb' ) ) as new_csv:
                for part in response.iter_content( chunk_size=256 ):
                    new_csv.write( part )
            print( "Download finalizado! O arquivo foi salvo em: {}".format( path ) )
        else:
            response.raise_for_status()
        