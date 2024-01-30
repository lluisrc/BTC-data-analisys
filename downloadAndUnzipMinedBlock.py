import requests
import gzip
from io import BytesIO

# Name of files tsv.gz from 'https://gz.blockchair.com/bitcoin/blocks'
data = """blockchair_bitcoin_blocks_20240106.tsv
blockchair_bitcoin_blocks_20240107.tsv
blockchair_bitcoin_blocks_20240108.tsv
blockchair_bitcoin_blocks_20240109.tsv
blockchair_bitcoin_blocks_20240110.tsv"""

data = data.split('\n')

def descargar_y_descomprimir(url, ruta_destino):
    try:
        # Realizar la solicitud GET al enlace
        respuesta = requests.get(url)
        
        # Verificar si la solicitud fue exitosa (código 200)
        if respuesta.status_code == 200:
            # Descomprimir el archivo gz
            contenido_comprimido = BytesIO(respuesta.content)
            with gzip.GzipFile(fileobj=contenido_comprimido, mode='rb') as archivo_comprimido:
                # Guardar el contenido descomprimido en la ruta especificada
                with open(ruta_destino, 'wb') as archivo_destino:
                    archivo_destino.write(archivo_comprimido.read())
            print(f"Archivo descargado y descomprimido con éxito en {ruta_destino}")
        else:
            print(f"Error al descargar el archivo. Código de estado: {respuesta.status_code}")
    except Exception as e:
        print(f"Error: {e}")

for i in data:
    descargar_y_descomprimir('https://gz.blockchair.com/bitcoin/blocks/'+i, 'dataset/'+i[:-3])
