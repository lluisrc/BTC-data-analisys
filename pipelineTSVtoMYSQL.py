import csv
import mysql.connector
from datetime import datetime

# Conexion to mysql
conexion = mysql.connector.connect(
    host="192.168.178.53",
    user="lroca",
    password="lroca",
    database="BTC_blocks"
)



# Name of the table
tabla = "BTC_blocks"

# Insert command
consulta_insercion = f"INSERT INTO {tabla} (id, hash, time, size, stripped_size, weight, version, nonce, difficulty, transaction_count, witness_count, input_count, output_count, input_total, input_total_usd, output_total, output_total_usd, cdd_total, generation, guessed_miner) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# Names of .tsv to insert get data and inserto into mysql
setDataTsv = """blockchair_bitcoin_blocks_20240106.tsv
blockchair_bitcoin_blocks_20240107.tsv
blockchair_bitcoin_blocks_20240108.tsv
blockchair_bitcoin_blocks_20240109.tsv
blockchair_bitcoin_blocks_20240110.tsv"""

files = setDataTsv.split('\n')

def leer_archivo_tsv(file):
    with open(file, 'r', newline='', encoding='utf-8') as archivo:
        lector_tsv = csv.reader(archivo, delimiter='\t')
        next(lector_tsv, None)
        for row in lector_tsv:
            id = int(row[0])
            hash = row[1]
            time = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
            size = int(row[4])
            stripped_size = int(row[5])
            weight = int(row[6])
            version = int(row[7])
            nonce = int(row[11])
            difficulty = int(round(float(row[13])))
            transaction_count = int(row[16])
            witness_count = int(row[17])
            input_count = int(row[18])
            output_count = int(row[19])
            input_total = int(row[20])
            input_total_usd = round(float(row[21]))
            output_total = int(row[22])
            output_total_usd = round(float(row[23]))
            cdd_total = round(float(row[30]), 2)
            generation = int(row[31])
            guessed_miner = row[35]

            datos = [id, hash, time, size, stripped_size, weight, version, nonce, difficulty, transaction_count, witness_count, input_count, output_count, input_total, input_total_usd, output_total, output_total_usd, cdd_total, generation, guessed_miner]
            
            cursor = conexion.cursor()
            cursor.execute(consulta_insercion, datos)
            print('File - ' + file + ' | block nº - ' + str(id))
            conexion.commit()
            cursor.close()

for i in files:
    leer_archivo_tsv('dataset2/'+i)

conexion.close()