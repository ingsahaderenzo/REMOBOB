import os
from clearer import clear_screen
from player import Player as pl


#Menu principal del juego
def main_menu():
    while True: #mostramos el menu principal y vemos hacia donde nos dirigiremos.
        clear_screen()
        try:
            decition = int(input('''
        Bienvenido a Remobob 
                                
        .:|Menu Principal|:. 
                                
        1) Iniciar Juego
        2) Ver reglas
        3) Ver estadísticas
        4) Opciones de guardado
        0) Salir del juego
                                
        Seleccione una opción: '''))
            if decition == 1: #Inicio del juego
                while True: #En este bucle seleccionaremos la dificultad que tendrá el juego
                    clear_screen()
                    nombre = input("Ingrese el nombre del primer jugador: ")
                    if nombre == "":
                        input("Porfavor no deje el nombre vacío, presione enter para reintentar")
                        continue
                    pl1 = pl(nombre)
                    nombre = input("Ingrese el nombre del segundo jugador: ")
                    if nombre == "":
                        input("Porfavor no deje el nombre vacío, presione enter para reintentar")
                        continue
                    pl2 = pl(nombre)
                    difficult = int(input('''
            Seleccione la dificultad con la que desea jugar:
            1) Personalizada (Máximo 10x10)
            3) Facil (3x3)
            5) Medio (5x5)
            7) Dificil (7x7)
            Ingrese decisión: '''))
                    if difficult == 1: #Esta opción es por si los jugadores eligen jugar con una dificultad personalidad
                        while True:
                            clear_screen()
                            row = int(input("Ingrese cantidad de filas: "))
                            column = int(input("Ingrese cantidad de columnas: "))
                            if row >10 or column>10: #Controlamos que haya como maximo 10 por un tema de dificultad de juego
                                input("Porfavor ingrese un valor menor a 10 para columnas o filas, presione enter para reintentar")
                                pass
                            break
                        break
                    elif (difficult == 3 or difficult == 5 or difficult == 7):
                        row , column = difficult, difficult #Para cualquier otra opción los valores serán iguales a la dificultad
                        break
                    else: 
                        input("Porfavor ingrese una de las opciones válidas, presione enter para reintentar")
            elif decition == 2: #Mostramos las reglas del juego y volvemos al meno principal
                clear_screen()
                print('''
    1) La idea del juego es revisar el casillero del otro jugador tratando de encontrar dos objetivos principales, 
    la contraseña y la bomba, ya que cuando encontremos el casillero donde se encuentra la bomba deberemos colocar la
    contraseña para poder abrir la caja fuerte y acceder a la bomba, una vez que abrimos la caja fuerte deberemos
    cortar el cable correcto para poder desarmarla, en caso de cortar otro cable perderemos instantaneamente.
          
    2) El juego cuenta con un sistema de calificación de desarmador de bombas, empezamos con 50 y por cada turno que
    juguemos se nos descontarán 5, al final de la partida se mostrará el puntaje del ganador y en base a eso se le dará un 
    título.
          
    3) Para poder navegar en el casillero se pedirá que ingresen primero un valor de fila y luego de columna. 
          
    4) En caso de encontrar la bomba y no tener la contraseña o no saber que cable cortar se contará con la posibiliad 
    de volver atrás para seguir buscando
                ''')
                input("\n\nCuando termine de leer las reglas presione enter")
            elif decition == 3: #Pendiente de completar
                pass 
            elif decition == 4: #Damos opciones para saber si quiere guardar los datos o no
                while True:
                    clear_screen()
                    save_decition = int(input("Desea guardar los datos del juego en un archivo local?\n1)Si\n2)No\nSeleccione una opción:"))
                    if save_decition == 1: #Si quiere le preguntamos la ruta donde desea guardar los datos
                        clear_screen()
                        rute = input("Ingrese la ruta donde desea guardar las estadísticas de juego: ")
                        if os.path.exists(rute): #Verificamos que la ruta exista y guardamos el dato
                            input("La ruta ingresada es válida, presione enter para voler al menu principal")
                            break
                        else: #Si no existe se la pedimos nuevamente
                            input("La ruta ingresada no existe, porfavor presione enter para reintentar")
                    elif save_decition == 2: #Si no quiere volvemos al menu principal
                        break
                    else: #En caso de seleccionar una opción invalida mostramos el mensaje de error y le pedimos de vuelta
                        input("Porfavor ingrese una de las opciones válidas, presione enter para reintentar")
            elif decition == 0: #Cerramos el juego
                os.system("cls")
                input("Gracias por jugar, porfavor presione enter para cerrar el juego")
                break
            else: #Pedimos que ingrese un valor que sea de las opciones validas
                input("Porfavor ingrese una de las opciones válidas, presione enter para reintentar")
        except ValueError: #Error que se mostrará en caso de ingresar un tipo de dato erroneo
            input("\n\nPorfavor ingrese un número entero, presione enter para reintentar")


if __name__=="__main__":
    main_menu()