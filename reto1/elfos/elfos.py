class Test1:
    def __init__(self):
        pass

    def darMaximoCalorias(self):
        suma = 0
        self.maximo = 0
        with open('/home/juanjo/adventofcode/reto1/input.txt', 'r') as f:
            lista = []
            for linea in f:
                if linea != '\n':
                    lista.append(int(linea.rstrip()))
                
                else:
                    suma = sum(lista)
                    if suma > self.maximo:
                        self.maximo = suma
                    lista.clear()
                    suma = 0
        
        return self.maximo

