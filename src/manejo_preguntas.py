#Seleccionar Preguntas al Azar

from itertools import combinations
from typing import List, Dict
import random

def select_combinations_with_unique_categories(questions: List[Dict[str, str]]) -> List[Dict[str, str]]:
    # Generar todas las combinaciones de 5 preguntas
    all_combinations = combinations(questions, 5)

    # Filtrar combinaciones donde todas las preguntas tienen categorías diferentes
    valid_combinations = list(filter(lambda comb: len(set(question['Category'] for question in comb)) == 5, all_combinations)) #Conjunto de categorías en la combinación tiene una longitud de 5, lo que implica que todas son diferentes.

    # Seleccionar una combinación aleatoria de las válidas
    if valid_combinations:
        return random.choice(valid_combinations)
    else:
        return []



