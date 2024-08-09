from clearer import clear_screen

class Player:
    def __init__(self,name):
        self.name = name #Nombre del jugador
        self.games = 0 #Cantidad de partidas del jugador
        self.wins = 0 #Cantidad de partidas ganadas por el jugador
        self.maxp = 0 #puntaje máximo del jugador
        self.bomb = 0 #Ubicación de la bomba, se actualizará en cada partida
        self.points = 50 #Puntos de desarmador, se actualizará en cada partida
        self.pasw = 0 #contraseña de la caja fuerte, se actualizará en cada partida
        self.cable = 0 #cable de la bomba, se ctualizará en cada partida


    #Función creada especificamente para poder seleccionar donde se guarda un dato
    def __ubication(self, n, m, option): #Option es la variable que nos indicará que dato estamos ubicando
        while True:
            try:
                clear_screen()
                
                #Pedimos que ingrese tanto columna como fila 
                row = int(input(f"Porfavor seleccione en que fila desea guardar la {option}(entre 1 y {n}): "))
                column = int(input(f"Porfavor seleccione en que columna desea guardar la {option}(entre 1 y {m}): "))

                 #Verificamos que los valores estén dentro de los posibles
                if row > n or column > m or row < 1 or column < 1: #En caso de fallar los pedimos de vuelta
                    input("Los valores ingresados superan el valor máximo posible, presione enter para reintentar")
                    continue

                else: #En caso de que sean válidos devolveremos los datos
                    return row, column #Devolvemos tanto fila como columna
                
            #Manejamos los errores en caso de que pongan un tipo de dato erroneo   
            except TypeError: 
                input("El tipo de dato que ingrese debe ser un entero, presione enter para reintentar")


    #Función en la cual el jugador definirá sus datos de juego como contraseña, bomba, cable y sus ubicaciones
    def set_all(self, row, column):
        while True:
            try:
                clear_screen()
                input(f"Turno de {self.name}, presione enter para iniciar")

                #Pedimos la ubicación de la bomba
                bomb_r, bomb_c = self.__ubication(row,column,"bomba") 
                self.bomb = [bomb_r , bomb_c]

                #Pedimos la ubicación de la contraseña
                while True: 
                    pasw_r, pasw_c = self.__ubication(row,column,"contraseña") 
                    
                    #Verificamos que la ubicación no este ocrupada
                    if pasw_r == bomb_r and pasw_c == bomb_c: #En caso de estarlo la pediremos de vuelta
                        input("La ubicación ingresada ya contiene algo, presione enter para reintentar")
                        continue
                    else: #En caso de no estar ocupado salimos del bucle
                        break
                
                #Pedimos la contraseña de 3 digitos de la caja fuerte
                while True: 
                    clear_screen()
                    pasw = input("Ingrese la contraseña de la caja fuerte(de 3 digitos): ")

                    #Nos aseguramos de que la contraseña sea de 3 digitos
                    if len(pasw) != 3: #En caso de que la longitud sea distinta de 3 la pediremos de vuelta
                        input("La contraseña debe ser de 3 digitos, presione enter para reintentar")
                        continue
                    break
                self.pasw = [pasw_r,pasw_c,pasw] #Guardamos los datos de la contraseña, tanto su ubicación como su valor

                #Pedimos el color del cable y asignamos las variabes según sea el caso 
                while True:
                    clear_screen()
                    cable = int(input("Seleccione que color es el que desactiva la bomba: \n1) Rojo\n2) Verde\n3) Azul\n Decisión: "))
                    if cable == 1:
                        color = "Rojo"
                        break
                    elif cable == 2:
                        color = "Verde"
                        break
                    elif cable == 3:
                        color = "Azul"
                        break
                    else: #En caso de ingresar un valor que no es opción mostraremos un error
                        input("El valor ingresado no se corresponde con ningún color, presione enter para reintentar")
                        continue

                #Pedimos la ubicación del cable
                while True:
                    cable_r, cable_c = self.__ubication(row,column,"opcion de cable correcta") 

                    #Verificamos que la ubicación ingresada no esté ocupada por el cable o la bomba
                    if (cable_r == bomb_r and cable_c == bomb_c) or (cable_c == pasw_c and cable_r == pasw_r):#En caso de estar ocupada la pedimos de vuelta
                        input("La ubicación ingresada ya tiene almacenado algo, presione enter para reintentar")
                        continue
                    else:
                        break
                self.cable = [cable_r,cable_c,cable,color] #Guardamos tanto la ubicación como el número del color y el color

                #Mostramos los datos en pantalla
                input(f''' 
            Los datos finales son:
            Bomba = columna: {self.bomb[1]}  fila: {self.bomb[0]}
            Contraseña = columna: {self.pasw[1]}  fila: {self.pasw[0]}  valor: {self.pasw[2]}
            Cable = columna: {self.cable[1]}  fila: {self.cable[0]}  color: {self.cable[3]}

            Presione enter para finalizar revisión
            ''')
                break

            #Excepción que se mostrará en caso de ingresar otro tipo de dato
            except ValueError:
                input("El tipo de dato que ingrese debe ser un entero, presione enter para reintentar")

    def play(self,n,m,rival):
        while True:
            try:
                clear_screen()
                input(f"Es el turno de {self.name}, porfavor pasenele el control, presione enter para seguir jugando")
                while True:
                    clear_screen()
                    row = int(input("Porfavor ingrese fila a la que desea moverse: "))
                    column = int(input("Porfavor ingrese columna a la que desea moverse: "))
                    if row > n or column > m or row < 1 or column < 1:
                        input("Los valores ingresados superan el valor máximo posible, presione enter para reintentar")
                        continue
                    break
                if row == rival.pasw[0] and column == rival.pasw[1]:
                    clear_screen()
                    input(f"Encontraste la contraseña de la caja fuerte, es {rival.pasw[2]} no lo olvides!\nPresione enter para pasar de turno")
                    return False
                elif row == rival.cable[0] and column == rival.cable[1]:
                    clear_screen()
                    input(f"Encontraste el color del cable a cortar, es {rival.cable[3]} no lo olvides!\nPresione enter para pasar de turno")
                    return False
                elif row == rival.bomb[0] and column == rival.bomb[1]:
                    pasword = input("Ingrese la contraseña de la caja fuerte: ")
                    if pasword != rival.pasw[2]:
                        input("Contraseña incorrecta, presione enter para pasar de turno")
                        return False
                    while True:
                        clear_screen()
                        cable = int(input('''
                                La contraseña que ingresaste es la correcta, ves como la puerta de la caja fuerte se abre lentamente
                                Al abrirse encuentras la bomba que estabas buscando, pero para desactivarla deberás cortar uno de los 3 cables,
                                debes saber que en caso de equivocarte la bomba explotará instantaneamente, puedes intentar cortar el cable ahora
                                o no hacer nada y volver cuando estes seguro de que hacer. Ingrese su decisión:
                                    1) Cortar cable rojo
                                    2) Cortar cable verde
                                    3) Cortar cable azul
                                    0) Pasar el turno sin cortar un cable
                                      
                                    Ingrese decisión: '''))
                        if cable == rival.cable[2]:
                            clear_screen()
                            input(f'''
                                Felicidades, cortaste el cable correcto y desactivaste la bomba antes que el rival.
                                SOS EL GANADOR con {self.points} puntos''')
                            if self.points > self.maxp:
                                self.maxp = self.points
                            return True
                        elif cable == 0:
                            clear_screen()
                            input("\nDecidiste irte sin hacer nada, presione enter para pasar el turno")
                            return False
                        elif cable < 1 or cable > 3:
                            clear_screen()
                            input("\nEl valor que ingresaste no corresponde con una opción disponible, presione enter para reintentar")
                            continue
                        else:
                            clear_screen()
                            input("\nOH NO CORTASTE EL CABLE INCORRECTO, BOOOOOOOOOM, MORISTE")
                            return True
                else:
                    if self.points == 0:
                        input("Te tardaste demasiado en desactivar esa bomba, vuelve a la base, tienes 0 puntos de desactivador y serás despedido")
                        return True
                    self.points -= 5
                    input(f"En esa ubicación no hay nada, ahora tienes {self.points} puntos, presione enter para pasar el turno")
                    return False
            except ValueError:
                input("El tipo de dato que ingrese debe ser un entero, presione enter para reintentar")