from remobob import clear_screen

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
                input("Los valores ingresados superan el valor máximo posible, presione enter para reintentar")
            except:
                input("El tipo de dato que ingrese debe ser un entero, presione enter para reintentar")

    #Función en la cual el jugador definirá sus datos de juego como contraseña, bomba, cable y sus ubicaciones
    def set_all(self, row, column):
        while True:
            try:
                bomb_r, bomb_c = self.__ubication(row,column,"bomba") #Pedimos la ubicación de la bomba
                self.bomb = [bomb_r , bomb_c]
                while True: #Se le pedirá que coloque la contraseña de 3 digitos
                    pasw = input("Ingrese la contraseña de la caja fuerte(de 3 digitos): ")
                    if len(pasw) != 3: #nos aseguramos de que la contraseña sea de 3 digitos
                        input("La contraseña debe ser de 3 digitos, presione enter para reintentar")
                    break
                pasw_r, pasw_c = self.__ubication(row,column,"contraseña") #Pedimos la ubicación de la contraseña
                self.pasw = [pasw_r,pasw_c,pasw]
                #Pedimos el color del cable a cortar
                cable = input("Seleccione que color es el que desactiva la bomba: \n1) Rojo\n2) Verde\n3) Azul\n Decisión: ")
                if cable == "1":
                    color = "Rojo"
                elif cable == "2":
                    color = "Verde"
                elif cable == "3":
                    color = "Azul"
                else:
                    input("El valor ingresado no se corresponde con ningún color, presione enter para reintentar")
                    pass
                cable_r, cable_c = self.__ubication(row,column,"opcion de cable correcta") #Pedimos la ubicación del cable
                self.cable = [cable_r,cable_c,cable,color]
                input(f''' 
            Los datos finales son:
            Bomba = columna:{self.bomb[1]}  fila:{self.bomb[0]}
            Contraseña = columna:{self.pasw[1]}  fila:{self.pasw[0]}  valor:{self.pasw[2]}
            Cable = columna:{self.cable[1]}  fila:{self.cable[0]}  color:{self.cable[3]}

            Presione enter para finalizar revisión''') #mostramos los datos finales y pasamos al siguietne paso
                break
            except ValueError:
                input("El tipo de dato que ingrese debe ser un entero, presione enter para reintentar")