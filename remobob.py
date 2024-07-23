import os

#Definición de funciones

#Limpia la pantalla según el sistema operativo.
def clear_screen(): 
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux y MacOS
        os.system('clear')

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
            if decition == 1: #Pendiente de completar
                pass
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
                    decition = int(input("Desea guardar los datos del juego en un archivo local?\n1)Si\n2)No\nSeleccione una opción:"))
                    if decition == 1: #Si quiere le preguntamos la ruta donde desea guardar los datos
                        clear_screen()
                        rute = input("Ingrese la ruta donde desea guardar las estadísticas de juego: ")
                        if os.path.exists(rute): #Verificamos que la ruta exista y guardamos el dato
                            input("La ruta ingresada es válida, presione enter para voler al menu principal")
                            break
                        else: #Si no existe se la pedimos nuevamente
                            input("La ruta ingresada no existe, porfavor presione enter para reintentar")
                    elif decition == 2: #Si no quiere volvemos al menu principal
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