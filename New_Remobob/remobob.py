import os
import pandas as pd
from clearer import clear_screen #Clear screen es una función que nos permite limpiar la terminal
from player import Player as pl


# Función que se encarga de guardar los datos de la partida
def save_game(player, dif): #Esperamos un objeto del tipo player además de el nivel de dificultad

    #Intercambiamos el número de dificultad por el nombre correspondiente
    if dif == 1:
        difficult = "Personalizada"
    elif dif == 3:
        difficult = "Fácil"
    elif dif == 5:
        difficult = "Medio"
    elif dif == 7: 
        difficult == "Dificil"

    while True:
        try:
            while True:
                clear_screen()

                #Preguntamos si desean guardar los resultados del ganador o no
                deci = int(input("Desea guardar los resultados del ganador ?\n\n1) Si\n2) No\nDecisión: "))

                if deci == 2: #En caso de no guardar nos despedimos y cerramos el juego
                    input("Gracias por jugar, presione enter para cerrar el juego")
                    os._exit(0)

                elif deci != 1: #En caso de colocar un valor no válido pedimos que ingrese otro
                    input("Porfavor ingrese una de las opciones validas, presione entere para reintentar")
                    continue

                #En caso de entrar al else es porque desea guardar la partida
                else:
                    while True:
                        while True:
                            clear_screen()

                            #Primero verificamos si existe el archivo que contiene la ruta para guardar los datos
                            if os.path.exists("save_rute.txt"): 
                                #En caso de existir leemos el archivo en una variable
                                with open("save_rute.txt", 'r') as archivo:
                                    rute = archivo.read()
                                break
                            
                            #En caso de no existir procederemos a pedirlo
                            else:
                                rute = input("Ingrese la ruta donde desea guardar las estadísticas de juego: ")
                                if os.path.exists(rute): #Verificamos que exista la ruta
                                    with open("save_rute.txt", "w") as archivo: 
                                        archivo.write(rute) #Si existe creamos un archivo txt y guardamos la ruta en su interior
                                    break
                                else: #Si no existe se la pedimos nuevamente
                                    input("La ruta ingresada no existe, porfavor presione enter para reintentar")
                                    continue
                        
                        #Creamos la nueva linea con los datos de la partida actual
                        df = pd.DataFrame([{
                            'Nombre' : player.name,
                            'Puntaje' : player.maxp,
                            'Dificultad' : difficult
                        }])

                        #Creamos la ruta donde se guardarán los datos del juego
                        ruta_final = os.path.join(rute,"remobob_estat.csv")

                        #Verificamos que dicha ruta exista y actuamos en base a eso
                        if not os.path.exists(ruta_final): #Si no existe previamente el archivo lo crearemos ahora amismo
                            df.to_csv(ruta_final,index=False)

                        #En caso de existir el archivo solamente agregaremos los datos al final
                        else:
                            df.to_csv(ruta_final,mode='a', header=False, index=False)
                        
                        #Mostramos mensaje final y cerramos el juego
                        input("Partida guardada exitosamente, presione enter para cerrar el juego")
                        os._exit(0)
        
        #Excepción en caso de equivocarse en tipo de dato
        except ValueError:
            input("\n\nPorfavor ingrese un número entero, presione enter para reintentar")


#Función que se usa para mostrar datos finales
def show_results(plw):
    clear_screen()
    input(f'''
            Para que el perdedor sepa, los datos del rival son:
            
            Bomba = columna: {plw.bomb[1]}  fila: {plw.bomb[0]}
            Contraseña = columna: {plw.pasw[1]}  fila: {plw.pasw[0]}  valor: {plw.pasw[2]}
            Cable = columna: {plw.cable[1]}  fila: {plw.cable[0]}  color: {plw.cable[3]}

            Presione enter para finalizar revisión            
''')


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
                                continue
                            break
                    elif (difficult == 3 or difficult == 5 or difficult == 7):
                        row , column = difficult, difficult #Para cualquier otra opción los valores serán iguales a la dificultad
                    else: 
                        input("Porfavor ingrese una de las opciones válidas, presione enter para reintentar")
                        continue
                    pl1.set_all(row,column)
                    pl2.set_all(row,column)
                    while True:
                        if pl1.play(row,column,pl2):
                            if pl1.points == 0:
                                show_results(pl2)
                                input("\n\nPreione enter para cerrar el juego")
                                os._exit(0)
                            show_results(pl1)
                            save_game(pl1, difficult)
                        elif pl2.play(row,column,pl1):
                            if pl2.points == 0:
                                show_results(pl1)
                                input("\n\nPreione enter para cerrar el juego")
                                os._exit(0)
                            show_results(pl2)
                            save_game(pl2, difficult)
                        else:
                            continue
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
                clear_screen()
                if os.path.exists("save_rute.txt"):
                    with open ("save_rute.txt" , 'r') as archivo:
                        rute = archivo.read()
                else:
                    input("Aun no se han guardado partidas en este juego, presione enter para volver al menu principal")
                    continue
                ruta_final = os.path.join(rute,"remobob_estat.csv")
                df = pd.read_csv(ruta_final)
                df_ord = df.sort_values("Puntaje", ascending= False)
                print(df_ord)
                input("\nPresione enter para volver al menu principal")
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