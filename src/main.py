def imprimirMensajeBienvenida():
    menuPrincipal = """
==================================================================
      ¡Bienvenidos al juego de Trivia más divertido!
==================================================================

¡Prepárate para un desafío de trivia lleno de diversión!

En este juego, tendrás la oportunidad de jugar una ronda con 5 preguntas al azar. 
Las preguntas pueden provenir de la misma categoría o de diferentes, según tu preferencia.

Elige una de las siguientes opciones para comenzar:

  1. Jugar ronda con una categoría al azar
  2. Jugar ronda con una categoría específica
  3. Jugar ronda con todas las categorías al azar
  4. Finalizar el programa

===================================================================
    """

    print("\n", menuPrincipal)

if __name__ == "__main__":
    opcion = 0

    while opcion != 5:

        imprimirMensajeBienvenida()
        try:
            opcion = int(input("Seleccione la opción deseada: "))

            if opcion == 1:
                pass

            elif opcion == 2:
                pass

            elif opcion == 3:
                pass

            elif opcion == 4:
                print("Su programa ha sido finalizado con exito")
                break

            else:
                print("Debe ingresar numeros del 1 al 5")

        except:
            print("La opción ingresada no era correcta. Intente nuevamente con un número.")