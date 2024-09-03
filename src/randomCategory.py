import random
from itertools import chain

def generar_preguntas_random(preguntas, cantidad=5):
    # Seleccionar 20 preguntas aleatorias del total
    preguntas_20 = random.sample(preguntas, min(20, len(preguntas)))
    
    # Seleccionar 5 preguntas aleatorias de esas 20 preguntas
    preguntas_5 = random.sample(preguntas_20, min(cantidad, len(preguntas_20)))
    
    return preguntas_5


def obtener_preguntas_por_categoria(preguntas, categoria):
    # Definir el predicado para filtrar preguntas por categoría
    igual_categoria = lambda pregunta: pregunta[0] == categoria
    # Aplicar filter con el predicado
    preguntas_filtradas = filter(igual_categoria, preguntas)
    # Convertir el iterador resultante en una lista
    return list(preguntas_filtradas)


def generar_opciones(pregunta_actual, preguntas_categoria, cantidad_opciones=4):
    respuesta_correcta = list(pregunta_actual[2])
    # Filtrar respuestas incorrectas usando filter y lambda
    respuestas_incorrectas = list(filter(lambda pregunta: pregunta!= pregunta_actual, preguntas_categoria))
    
    # Usar map para extraer las respuestas incorrectas
    respuestas_incorrectas = list(map(lambda pregunta: pregunta[2], respuestas_incorrectas))
    
    # Generar opciones incluyendo la respuesta correcta
    opciones = list(chain(respuesta_correcta, random.sample(respuestas_incorrectas, min(cantidad_opciones - 1, len(respuestas_incorrectas)))))
    '''
    min(cantidad_opciones - 1, len(respuestas_incorrectas)): Aseguramos que la muestra de respuestas incorrectas tome hasta tres elementos, 
    o menos si no hay suficientes respuestas incorrectas disponibles.
    '''
    # Mezclar las opciones aleatoriamente
    return random.sample(opciones, len(opciones))


def mostrar_pregunta(pregunta_actual, opciones):
    # Funciones lambda para imprimir la categoría y la pregunta
    mostrar_categoria = lambda pregunta_categoria: print(f"\nCategoría: {pregunta_categoria[0]}")
    mostrar_pregunta = lambda pregunta_letra: print(f"Pregunta: {pregunta_letra[1]}")
    
    # Mostrar categoría y pregunta
    mostrar_categoria(pregunta_actual)
    mostrar_pregunta(pregunta_actual)
    
    print("Opciones:")
    
    # Enumerar y mostrar las opciones usando map y una función lambda
    enumerate_opciones = lambda idx_opcion: print(f"{idx_opcion[0]}. {idx_opcion[1]}")
    list(map(enumerate_opciones, enumerate(opciones, start=1)))
    
    # Capturar la respuesta del usuario y yield
    respuesta_usuario = input("Selecciona tu respuesta (1, 2, 3, 4): ")
    yield respuesta_usuario


def verificar_respuesta(respuesta_usuario, respuesta_correcta):
    return respuesta_usuario.strip.lower() == respuesta_correcta.strip.lower()


def procesar_pregunta(pregunta, opciones):
    '''
    Quiero hacer que por cada pregunta:
    Si la respuesta es correcta se le den 10 puntos al jugador y pase a siguiente pregunta
    Si la respuesta no es correcta, se le de otra chance
    Si en la segunda chance le emboca, se le den 5 puntos
    Si en la segunda chance no emboca, se le den 0 puntos  y pase a siguiente pregunta

    USAR RECURSION para incorporar en la verificación de respuestas para reintentar hasta el segundo intento.
    USAR MOANDS con logs para ir guardando el puntaje del jugador
    '''
    pass

'''
FALTAN DECORADORES:
    - Puntaje: es un decorador que muestra el puntaje acumulado después de cada ronda. 
    - Temporizador: decorador para ver el tiempo de respuesta del usuario.

FALTA HACER EL TIPADO

FALTA HACER DOCSTRING

FALTAN TESTS: haya una cobertura de tests de al menos 85%. 
'''





'''
# Función para seleccionar una categoría aleatoria
def select_random_category(categories):
    return random.choice(categories)

# Función para filtrar preguntas de una categoría específica
def filter_by_category(rows, category):
    return list(filter(lambda row: row['Category'] == category, rows))

# Función para seleccionar preguntas aleatorias
def select_random_questions(questions, num_questions=5):
    return random.sample(questions, num_questions)

# Función para generar opciones de respuesta múltiples en una categoría específica
def generate_multiple_choice_options(rows, category, correct_answer, num_options=4):
    # Filtrar filas de la misma categoría
    same_category_rows = list(filter(lambda row: row['Category'] == category, rows))
    
    # Obtener respuestas incorrectas de la misma categoría
    all_answers = list(map(lambda row: row['Answer'], filter(lambda row: row['Answer'] != correct_answer, same_category_rows)))
    
    # Seleccionar respuestas incorrectas al azar
    random_answers = random.sample(all_answers, num_options - 1)
    
    # Combinar respuestas incorrectas con la correcta usando itertools.chain
    options = list(chain(random_answers, [correct_answer]))
    
    # Mezclar las opciones
    random.shuffle(options)
    
    return options

# Función para crear una ronda de trivia usando programación funcional
def create_trivia_round(file_path):
    rows = read_csv(file_path)
    
    # Extraer categorías únicas
    categories = extract_categories(rows)
    selected_category = select_random_category(categories)
    
    # Filtrar preguntas de la categoría seleccionada
    questions = filter_by_category(rows, selected_category)
    selected_questions = select_random_questions(questions)
    
    # Crear preguntas para la ronda
    round_questions = list(map(lambda question: {
        'question': question['Question'],
        'options': generate_multiple_choice_options(rows, selected_category, question['Answer']),
        'correct_answer': question['Answer']
    }, selected_questions))

    return selected_category, round_questions

def print_question_with_options(question_data):
    question_text = f"Pregunta: {question_data['question']}"
    options = question_data['options']
    options_text = '\n'.join(f"{chr(ord('a') + idx)}) {option}" for idx, option in enumerate(options))
    return f"{question_text}\n{options_text}"

def get_user_answer():
    return input("Ingrese su respuesta (a, b, c, d): ").strip().lower()

def check_answer(user_answer, question_data):
    options = question_data['options']
    correct_answer = question_data['correct_answer']
    if user_answer in 'abcd' and options[ord(user_answer) - ord('a')] == correct_answer:
        return "\n ¡Correcto! :D"
    return f"\n Incorrecto :( La respuesta correcta es: {correct_answer}"

def play_trivia_round(file_path):
    selected_category, trivia_round = create_trivia_round(file_path)
    print(f"Categoría en la que estás jugando: {selected_category}\n")
    
    def process_question(question_data):
        print(print_question_with_options(question_data))
        user_answer = get_user_answer()
        result = check_answer(user_answer, question_data)
        print(result)
        print()
    
    # Procesar cada pregunta en la ronda
    list(map(process_question, trivia_round))

# Llamar a la función para jugar la ronda de trivia
file_path = 'datos/questions.csv'
play_trivia_round(file_path)
'''