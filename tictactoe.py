import random
import time



jugadasPosibles = {"1":"1",
                    "2":"2",
                    "3":"3",
                    "4":"4",
                    "5":"X",
                    "6":"6",
                    "7":"7",
                    "8":"8",
                    "9":"9"}

gameOn = True

posicionesNoUsadas = ["1","2","3","4","-","6","7","8","9"]





def printarBoard():
    print("+--------"*3,end="+\n")
    print("|        "*3, end="|\n")
    print("|  ",jugadasPosibles["1"],"   ", end="|")
    print("  ",jugadasPosibles["2"],"   ", end="|")
    print("  ",jugadasPosibles["3"],"   ", end="|\n")
    print("|        "*3, end="|\n")
    print("+--------"*3,end="+\n")
    print("|        "*3, end="|\n")
    print("|  ",jugadasPosibles["4"],"   ", end="|")
    print("  ",jugadasPosibles["5"],"   ", end="|")
    print("  ",jugadasPosibles["6"],"   ", end="|\n")
    print("|        "*3, end="|\n")
    print("+--------"*3,end="+\n")
    print("|        "*3, end="|\n")
    print("|  ",jugadasPosibles["7"],"   ", end="|")
    print("  ",jugadasPosibles["8"],"   ", end="|")
    print("  ",jugadasPosibles["9"],"   ", end="|\n")
    print("|        "*3, end="|\n")
    print("+--------"*3,end="+\n")

def comentarioInicial():
    print("Bienvenid@ al Tic Tac Toe Python,\nYo elegì el centro, ¿cual de los numeros es tu jugada?")

def jugadaPC(posicionesNoUsadas, jugadasPosibles):
    print("ahora vengo yo")
    time.sleep(2)
    
    jugadaPC = "O"
    while jugadaPC == "O":
        jugadaPC = random.choice(posicionesNoUsadas)
        if jugadaPC == "-" or jugadasPosibles[jugadaPC] == "O" or jugadasPosibles[jugadaPC]== "X":
            jugadaPC = "O"
    
    print("Yo elijo el: ",jugadaPC)
    print("Con ese numero marcado, el nuevo tablero es: ")
    jugadasPosibles[jugadaPC] = "X"
    posicionesNoUsadas[int(jugadaPC) -1 ]="-"
    printarBoard()
    

def jugadaPlayer(posicionesNoUsadas,jugadasPosibles):

    jugadaPlayer = "O"
    while jugadaPlayer == "O":
        jugadaPlayer = input("TU jugada, un numero del 1 al 9...")

        if jugadaPlayer.isnumeric():


            if int(jugadaPlayer)>0 and int(jugadaPlayer) < 10:
                if (jugadasPosibles[jugadaPlayer] == "O" or jugadasPosibles[jugadaPlayer]== "X"):
                    print("Ese ya fue escogido")
                    jugadaPlayer = "O"
            else:
                print("Ugh, nùmero inválido")
                jugadaPlayer = "O"
        else:
            print("Es un numero lo que debes jugar")   
            jugadaPlayer= "O"     
   
    if jugadaPlayer in posicionesNoUsadas:
        for i in range(len(posicionesNoUsadas)+2):
            if jugadaPlayer == posicionesNoUsadas[i]:
                print("Con el", jugadasPosibles[str(i+1)], "marcado, el nuevo tablero es: ")
                jugadasPosibles[str(i+1)] = "O"
                posicionesNoUsadas[i]="-"
                printarBoard()
                break

    else:       
        print("Ese ya fue elegido, ya està elegido o no es vàlido")
            

def ganoAlguien(jugadasPosibles):
    if jugadasPosibles["1"] == jugadasPosibles["2"] == jugadasPosibles["3"]:
        if jugadasPosibles["1"] == "X":
            print("Gané YO")
        else:
            print("Ganaste tu")
        return True
    if jugadasPosibles["4"] == jugadasPosibles["5"] == jugadasPosibles["6"]:
        if jugadasPosibles["4"] == "X":
            print("Gané YO")
        else:
            print("Ganaste tu")
        return True
    if jugadasPosibles["7"] == jugadasPosibles["8"] == jugadasPosibles["9"]:
        if jugadasPosibles["7"] == "X":
            print("Gané YO")
        else:
            print("Ganaste tu")
        return True
    if jugadasPosibles["1"] == jugadasPosibles["4"] == jugadasPosibles["7"]:
        if jugadasPosibles["1"] == "X":
            print("Gané YO")
        else:
            print("Ganaste tu")
        return True
    if jugadasPosibles["2"] == jugadasPosibles["5"] == jugadasPosibles["8"]:
        if jugadasPosibles["2"] == "X":
            print("Gané YO")
        else:
            print("Ganaste tu")
        return True
    if jugadasPosibles["3"] == jugadasPosibles["6"] == jugadasPosibles["9"]:
        if jugadasPosibles["3"] == "X":
            print("Gané YO")
        else:
            print("Ganaste tu")
        return True
    if jugadasPosibles["1"] == jugadasPosibles["5"] == jugadasPosibles["9"]:
        if jugadasPosibles["1"] == "X":
            print("Gané YO")
        else:
            print("Ganaste tu")
        return True
    if jugadasPosibles["3"] == jugadasPosibles["5"] == jugadasPosibles["7"]:
        if jugadasPosibles["3"] == "X":
            print("Gané YO")
        else:
            print("Ganaste tu")
        return True

def empate(jugadasPosibles):
    counter = 0
    for i in range(9):
        if jugadasPosibles[str(i+1)].isnumeric():
            counter += 1
    if counter>0:
        return False
    else:
        print("Parece que hay un empate")
        return True


comentarioInicial()
printarBoard()

while gameOn:
    jugadaPlayer(posicionesNoUsadas, jugadasPosibles)
    if ganoAlguien(jugadasPosibles) or empate(jugadasPosibles):
        break
    jugadaPC(posicionesNoUsadas, jugadasPosibles)
    if ganoAlguien(jugadasPosibles) or empate(jugadasPosibles):
        break



           
print("Fin del Juego")
