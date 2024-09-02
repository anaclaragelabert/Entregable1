import csv
import random

# Ruta al archivo CSV
file_path = 'datos/questions.csv'

# Abrir y leer el archivo CSV
def read_csv(file_path):
    with open(file_path, newline='', encoding='latin1') as archive:
        # Crear un generador de filas del archivo CSV
        reader = csv.reader(archive)
        # Convertir el generador en una lista utilizando map y list
        #rows = list(map(lambda row: dict(row), reader))
        
        headers = next(reader)
        print("Cabeceras:", headers)
    #return rows
read_csv(file_path)        
"""        
        reader = csv.reader(archive)

        # Leer y mostrar la cabecera
        headers = next(reader)
        print("Cabeceras:", headers)

        # Leer cada fila del CSV
        for row in reader:
           print(row)

read_csv(file_path)
"""

# Seleccionar un número específico de preguntas aleatorias de una lista
def select_random_questions(questions, num_questions=20):
    return random.sample(questions, num_questions)

def extract_categories(rows):
    # Utiliza map para extraer las categorías de cada fila
    categories = map(lambda row: row['Category'], rows)
    # Convertir el resultado en un conjunto para eliminar duplicados
    unique_categories = set(categories)
    # Convertir el conjunto a una lista
    return list(unique_categories)

#rows = read_csv(file_path)
#categories = extract_categories(rows)
#print("Categorías extraídas:", categories)

#No se por que cada vez que lo corro me pone diferentes categorias lol 
