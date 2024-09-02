import csv
from reader import read_csv

def extract_categories(file_path):
    categories = set()  # Usamos un conjunto para evitar duplicados

    with open(file_path, newline='', encoding='latin1') as archive:
        reader = csv.DictReader(archive)  # Utilizamos DictReader para acceder a las columnas por nombre
        
        for row in reader:
            category = row['Category']
            categories.add(category)  # Agregamos la categoría al conjunto

    return list(categories)  # Convertimos el conjunto a lista