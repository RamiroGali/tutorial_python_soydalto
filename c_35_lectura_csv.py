import csv

ruta_csv = "src\\csv_doc.csv"

with open(ruta_csv) as archivo:
    contenido = csv.reader(archivo)
    for row in contenido:
        print(row)
