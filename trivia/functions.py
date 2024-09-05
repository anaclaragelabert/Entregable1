import random
from itertools import chain
from typing import List, Dict, Tuple, Callable

def generar_preguntas_random(preguntas, cantidad_preguntas):
    preguntas_seleccionadas = random.sample(preguntas, cantidad_preguntas)
    for pregunta in preguntas_seleccionadas:
        yield pregunta


def generar_opciones(preguntas, pregunta_actual):
    respuesta_correcta = pregunta_actual[2]
    categoria_actual = pregunta_actual[0]

    # Filtrar preguntas que tengan la misma categoría pero una respuesta incorrecta
    respuestas_incorrectas = list(
        filter(
            lambda pregunta: pregunta[2] != respuesta_correcta and pregunta[0] == categoria_actual,
            preguntas
        )
    )

    if len(respuestas_incorrectas) < 2:
        # Si no hay suficientes respuestas incorrectas en la misma categoría, añadir respuestas incorrectas de otras categorías
        nuevas_incorrectas = list(
            filter(
                lambda pregunta: pregunta[2] != respuesta_correcta,
                preguntas
            )
        )
        nuevas_incorrectas = random.sample(nuevas_incorrectas, min(2, len(nuevas_incorrectas)))
        opciones = list(chain(nuevas_incorrectas, [pregunta_actual]))
    else:
        # Seleccionar 2 respuestas incorrectas de la misma categoría
        respuestas_seleccionadas = random.sample(respuestas_incorrectas, 2)
        opciones = list(chain([pregunta_actual], respuestas_seleccionadas))

    # Extraer solo las respuestas de las opciones
    return [opcion[2] for opcion in mezclar_opciones(opciones)]

def mezclar_opciones(opciones):
    opciones_copiadas = opciones[:]
    random.shuffle(opciones_copiadas)
    return opciones_copiadas

'''
def generar_opciones(preguntas, pregunta_actual):
    respuesta_correcta = pregunta_actual[2]
    respuestas_incorrectas = list(filter(lambda pregunta: pregunta[2] != respuesta_correcta and pregunta[0] == pregunta_actual[0]), preguntas)

    if len(respuestas_incorrectas) < 2:
        nuevas_incorrectas = random.sample(list(filter(lambda pregunta: pregunta[1] != respuesta_correcta), preguntas), 2)
        return list(chain(nuevas_incorrectas, [respuesta_correcta]))
    else:
        return list(chain([respuesta_correcta], random.sample(respuestas_incorrectas, 2))) 
    
def mezclar_opciones(opciones):
    return random.shuffle(opciones, len(opciones))
'''

def calcular_puntaje(respuestas_correctas: int) -> int:
    return respuestas_correctas * 10


def mostrar_pregunta(pregunta, opciones):
    print(f"\nCategoría: {pregunta[0]}")
    print(f"\nPregunta: {pregunta[1]}")

    for indice, opcion in enumerate(opciones):
        print(f"{indice + 1}. {opcion}")

    resupuesta_usuario = input("\nIngrese su respuesta (1, 2, 3): ")

    if resupuesta_usuario not in {'1', '2', '3'}:
        print("\nOpción inválida. Su respuesta debe ser 1, 2 o 3.")
        return mostrar_pregunta(pregunta, opciones)
    
    return resupuesta_usuario
    

MonadaResultado = Tuple[int, str]

def verificar_respuesta(pregunta: List[str], respuesta_usuario: int, opciones: List[str]) -> MonadaResultado:
    verificacion_res = lambda answer: answer.lower() == pregunta[2].lower()

    es_correcto = verificacion_res(opciones[respuesta_usuario - 1])
    log = f"\nCategoría: {pregunta[0]}\nPregunta: {pregunta[1]}\n"

    if es_correcto:
        log += "\n¡Correcto!\n"
        return 1, log
    else:
        log += f"\nIncorrecto. La respuesta correcta era: {pregunta[2]}\n"
        return 0, log

def bind(func: Callable[[int], MonadaResultado], monada: MonadaResultado) -> MonadaResultado:
    res = func(monada[0])
    return res[0], monada[1] + res[1]

def unit(valor: int) -> MonadaResultado:
    return valor, ""

def procesar_pregunta(pregunta: List[str], opciones: List[str], respuesta_usuario: int) -> Callable[[MonadaResultado], MonadaResultado]:
    return lambda estado: bind(lambda _: verificar_respuesta(pregunta, respuesta_usuario, opciones), estado)


#Esta bien usar for si lo que hace no afecta algo externo (CHEQUEAR QUE NO PASE ESTO)
def ejecutar_ronda(preguntas: List[List[str]], opciones: List[List[str]], respuestas_usuario: List[int]) -> List[str]:
    resultado_final = unit(0)
    
    # Procesar cada pregunta
    procesos = [procesar_pregunta(pregunta, opciones[i], respuestas_usuario[i]) for i, pregunta in enumerate(preguntas)]
    
    # Acumulando resultados y logs
    resultados = [resultado_final]
    for proceso in procesos:
        resultados.append(proceso(resultados[-1]))

    # Extraer logs
    logs = [res[1] for res in resultados[1:]]
    
    # Calcular puntaje total
    puntaje_total = calcular_puntaje(sum(res[0] for res in resultados[1:]))

    return logs + [f"\nResultado final: {puntaje_total}\n"]

