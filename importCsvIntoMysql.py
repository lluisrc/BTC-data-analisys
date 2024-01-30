import csv, os
import mysql.connector
from datetime import datetime

# Conexion to mysql
conexion = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)


# Name of the table
tabla = "BTC_price"

# Insert command
consulta_insercion = f"INSERT INTO {tabla} (day, price, open, high, low, vol, `change`) VALUES (%s, %s, %s, %s, %s, %s, %s)"

# Names of .csv to insert get data and inserto into mysql, este csv se obtiene de 'https://www.investing.com/crypto/bitcoin/historical-data'
dataCsv = """Bitcoin Historical Data.csv"""

with open(f"{dataCsv}", "r") as file:
    lector_csv = csv.reader(file)
    next(lector_csv)
    for row in lector_csv:
        print(row)
        day = datetime.strptime(row[0], '%m/%d/%Y').strftime('%Y/%m/%d')
        price = float(row[1].replace(',',''))
        open = float(row[2].replace(',',''))
        high = float(row[3].replace(',',''))
        low = float(row[4].replace(',',''))
        if (row[5] == ''):
            row[5] = 0
        elif (row[5][-1] == 'K'):
            vol = float(row[5][:-1])*1000
        elif (row[5][-1] == 'M'):
            vol = float(row[5][:-1])*1000*1000
        elif (row[5][-1] == 'B'):
            vol = float(row[5][:-1])*1000*1000*1000
        change = float(row[6][:-1])

        data = [day, price, open, high, low, vol, change]

        cursor = conexion.cursor()
        cursor.execute(consulta_insercion, data)
        conexion.commit()
        cursor.close()
