import string

def convertidorStringEnteros(intervalo):
    numeros = intervalo.split("-")
    return numeros

def main():
    contador = 0
    
    """
    with open('/home/juanjo/adventofcode/day4/input.txt', 'r') as f:
        lista = []
        for linea in f:
            lista.append(linea.rstrip().split(","))
        f.close()


    for list in lista:
        a = convertidorStringEnteros(list[0])
        b = convertidorStringEnteros(list[1])
        if int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1]):
            contador += 1
        elif int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1]):
            contador +=1
    print(contador)
    """
    with open('/home/juanjo/adventofcode/day4/input.txt', 'r') as f:
        lista = []
        for linea in f:
            lista.append(linea.rstrip().split(","))
        f.close()

    overlap = 0
    for list in lista:
        a = convertidorStringEnteros(list[0])
        b = convertidorStringEnteros(list[1])
        if int(a[0]) >= int(b[0]) and int(a[0]) <= int(b[1]):
            overlap += 1
        elif int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[0]):
            overlap += 1
    print(overlap)
if __name__ == '__main__':
    main()