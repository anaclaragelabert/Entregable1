import csv

# Ruta al archivo CSV
file_path = 'datos/questions.csv'

# Abrir y leer el archivo CSV
with open(file_path, newline='', encoding='latin1') as csvfile:
    reader = csv.reader(csvfile)

    # Leer y mostrar la cabecera
    headers = next(reader)
    print("Cabeceras:", headers)

    # Leer cada fila del CSV
    #for row in reader:
    #   print(row)
