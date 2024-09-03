from reader import extract_categories, read_csv
import random
from itertools import chain

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