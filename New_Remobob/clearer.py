import os

#Limpia la pantalla según el sistema operativo.
def clear_screen(): 
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux y MacOS
        os.system('clear')