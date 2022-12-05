import string

def darPuntuacionLetra(c):
    puntuacion = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, 
                    "p": 16,"q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
    if(c.isupper()):
        minuscula  = c.lower()
        return puntuacion[minuscula] + 26

    else: 
        return puntuacion[c]



def main():
    
    #Primera parte
    """
    suma_total = 0
    with open('/home/juanjo/adventofcode/day3/input.txt', 'r') as f:
        lista = []
        for linea in f:
            lista.append(linea.rstrip())
        f.close()
    
    palabra1 = ""
    palabra2 = ""
    for l in lista:
        palabra1 = l[:len(l)//2]
        palabra2 = l[len(l) // 2:]

        for i in palabra1:
            for j in palabra2:
                if i == j:
                    letra = i
        suma_total += darPuntuacionLetra(letra) 
    print(suma_total)
    """

    #Segunda parte

    contador = 1
    suma_total = 0
    with open('/home/juanjo/adventofcode/day3/input.txt', 'r') as f:
        lista_3_elfos = []
        lista = []
        for linea in f:
            lista.append(linea.rstrip())
            if contador % 3 == 0:
                lista_3_elfos.append(lista)
                lista = []
            contador = contador + 1
        f.close()

    for lista in lista_3_elfos:
        palabra1 = lista[0]
        palabra2 = lista[1]
        palabra3 = lista[2]
        for i in palabra1:
            for j in palabra2:
                if i == j:
                    letra = i
                    for k in palabra3:
                        if(letra == k):
                            letradefinitiva = k 
        suma_total += darPuntuacionLetra(letradefinitiva)   
    
    print(suma_total)
if __name__ == '__main__':
    main()