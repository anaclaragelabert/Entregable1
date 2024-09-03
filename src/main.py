def imprimirMensajeBienvenida() -> None:
    menuPrincipal = """
==================================================================
      ¡Bienvenidos al juego de Trivia más divertido!
==================================================================

¡Prepárate para un desafío de trivia lleno de diversión!

En este juego, tendrás la oportunidad de jugar una ronda con 5 preguntas al azar. 

Elige una de las siguientes opciones para comenzar:

  1. Jugar ronda con todas las categorías al azar
  2. Finalizar el programa

===================================================================
    """

    print("\n", menuPrincipal)



if __name__ == "__main__":
    opcion = 0

    while opcion != 2:

        imprimirMensajeBienvenida()
        try:
            opcion = int(input("Seleccione la opción deseada: "))

            if opcion == 1:
                pass

            elif opcion == 2:
                print("Su programa ha sido finalizado con exito")
                break

            else:
                print("Debe ingresar numeros del 1 al 2")

        except:
            print("La opción ingresada no era correcta. Intente nuevamente con un número.")