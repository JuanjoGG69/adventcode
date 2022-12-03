#Contrincante: Rock -> A, Paper -> B, Scissors -> C
#Yo: Rock -> X, Paper -> Y, Scissors -> Z

def darPuntuacionVictEmpDerr(a, b):
    puntuacion = 0
    if a == 'A':
        if b == 'X':
            puntuacion = 3
        elif b == 'Y':
            puntuacion = 6
        elif b == 'Z':
            puntuacion = 0
    
    elif a == 'B':
        if b == 'X':
            puntuacion = 0
        elif b == 'Y':
            puntuacion = 3
        elif b == 'Z':
            puntuacion = 6
    elif a == 'C':
        if b == 'X':
            puntuacion = 6
        elif b == 'Y':
            puntuacion = 0
        elif b == 'Z':
            puntuacion = 3
    return puntuacion

def darPuntuacionTest2(a, b, movimientos):
    puntuacion = 0
    if a == 'A':
        if b == 'X':
            puntuacion =  int(movimientos['Z'])
        elif b == 'Y':
            puntuacion = 3 + int(movimientos['X'])
        elif b == 'Z':
            puntuacion = 6 + int(movimientos['Y'])
    if a == 'B':
        if b == 'X':
            puntuacion =  int(movimientos['X'])
        elif b == 'Y':
            puntuacion = 3 + int(movimientos['Y'])
        elif b == 'Z':
            puntuacion = 6 + int(movimientos['Z'])
    if a == 'C':
        if b == 'X':
            puntuacion =  int(movimientos['Y'])
        elif b == 'Y':
            puntuacion = 3 + int(movimientos['Z'])
        elif b == 'Z':
            puntuacion = 6 + int(movimientos['X'])
    
    return puntuacion

def main():
    
    #FIRST TEST
    """
    with open('/home/juanjo/adventofcode/day2/input.txt', 'r') as f:
        suma_total = 0

        #We read the input and save in a list
        lista = []
        for linea in f:
            lista.append(linea.rstrip().split())

        #We create a dictionary, the key is A,B or C y the values their scores
        movimientos = {'X': 1, 'Y': 2, 'Z': 3}

        for list in lista:
            if list[1] == 'X': 
                puntuacion = movimientos['X']
            elif list[1] == 'Y':
                puntuacion = movimientos['Y']
            elif list[1] == 'Z':
                puntuacion = movimientos['Z']

            suma_total += puntuacion + darPuntuacionVictEmpDerr(list[0], list[1])

        print(suma_total)
    """

    #SECOND TEST
    #Yo: X -> lose, Y -> draw, Z -> win
    suma_total = 0
    with open('/home/juanjo/adventofcode/day2/input.txt', 'r') as f:
        lista = []
        movimientos = {'X': 1, 'Y': 2, 'Z': 3}
        for linea in f:
            lista.append(linea.rstrip().split())

        for list in lista:
            suma_total += darPuntuacionTest2(list[0], list[1], movimientos)
        
        print(suma_total)

if __name__ == '__main__':
    main()