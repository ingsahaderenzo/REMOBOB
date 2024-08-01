from clearer import clear_screen

class Player:
    def __init__(self,name):
        self.name = name #Nombre del jugador
        self.games = 0 #Cantidad de partidas del jugador
        self.wins = 0 #Cantidad de partidas ganadas por el jugador
        self.max = 0 #puntaje máximo del jugador
        self.bomb = 0 #Ubicación de la bomba, se actualizará en cada partida
        self.points = 50 #Puntos de desarmador, se actualizará en cada partida
        self.pasw = 0 #contraseña de la caja fuerte, se actualizará en cada partida
        self.cable = 0 #cable de la bomba, se ctualizará en cada partida


    #Función creada especificamente para poder seleccionar donde se guarda un dato
    def __ubication(self, n, m, option):
        while True:
            try:
                clear_screen()
                row = int(input(f"Porfavor seleccione en que fila desea guardar la {option}(entre 1 y {n}): "))
                column = int(input(f"Porfavor seleccione en que columna desea guardar la {option}(entre 1 y {m}): "))
                if row <= n or column <= m: #Verificamos que los valores estén dentro de los posibles
                    return row, column #Devolvemos tanto fila como columna
                else:
                    input("Los valores ingresados superan el valor máximo posible, presione enter para reintentar")
                    continue
            except TypeError: #Manejamos los errores en caso de que pongan un tipo de dato erroneo
                input("El tipo de dato que ingrese debe ser un entero, presione enter para reintentar")


    #Función en la cual el jugador definirá sus datos de juego como contraseña, bomba, cable y sus ubicaciones
    def set_all(self, row, column):
        while True:
            try:
                #Empezamos pidiendo la ubicación de la bomba
                bomb_r, bomb_c = self.__ubication(row,column,"bomba") 
                self.bomb = [bomb_r , bomb_c]

                #Pedimos la ubicación de la bomba
                while True: 
                    pasw_r, pasw_c = self.__ubication(row,column,"contraseña") 
                    if pasw_r == bomb_r and pasw_c == bomb_c: #Vereificamos que no sean posiciones ocupadas
                        input("La ubicación ingresada ya contiene algo, presione enter para reintentar")
                        continue
                    else: #En caso de estar ocupado las pedimos de vuelta
                        break
                
                #Pedimos la contraseña de 3 digitos de la caja fuerte
                while True: 
                    clear_screen()
                    pasw = input("Ingrese la contraseña de la caja fuerte(de 3 digitos): ")
                    if len(pasw) != 3: #Nos aseguramos de que la contraseña sea de 3 digitos
                        input("La contraseña debe ser de 3 digitos, presione enter para reintentar")
                        continue
                    break
                self.pasw = [pasw_r,pasw_c,pasw]

                #Pedimos el color del cable a cortar
                while True:
                    clear_screen()
                    cable = input("Seleccione que color es el que desactiva la bomba: \n1) Rojo\n2) Verde\n3) Azul\n Decisión: ")
                    if cable == "1":
                        color = "Rojo"
                        break
                    elif cable == "2":
                        color = "Verde"
                        break
                    elif cable == "3":
                        color = "Azul"
                        break
                    else:
                        input("El valor ingresado no se corresponde con ningún color, presione enter para reintentar")
                        continue

                #Pedimos la ubicación del cable
                while True:
                    cable_r, cable_c = self.__ubication(row,column,"opcion de cable correcta") #Pedimos la ubicación del cable
                    if (cable_r == bomb_r and cable_c == bomb_c) or (cable_c == pasw_c and cable_r == pasw_r):
                        input("La ubicación ingresada ya tiene almacenado algo, presione enter para reintentar")
                        continue
                    else:
                        break
                self.cable = [cable_r,cable_c,cable,color]

                #Mostramos los datos en pantalla
                input(f''' 
            Los datos finales son:
            Bomba = columna: {self.bomb[1]}  fila: {self.bomb[0]}
            Contraseña = columna: {self.pasw[1]}  fila: {self.pasw[0]}  valor: {self.pasw[2]}
            Cable = columna: {self.cable[1]}  fila: {self.cable[0]}  color: {self.cable[3]}

            Presione enter para finalizar revisión''') #mostramos los datos finales y pasamos al siguietne paso
                break

            except ValueError: #Excepción que se mostrará en caso de ingresar otro tipo de dato
                input("El tipo de dato que ingrese debe ser un entero, presione enter para reintentar")


player = Player("Renzo")
player.set_all(3,3)