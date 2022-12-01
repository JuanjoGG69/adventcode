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

    def darSumatoriaMaximasCalorias(self):
        lista = []
        lista_sumas = []
        elfos_mas_calorias = []
        with open('/home/juanjo/adventofcode/reto1/input.txt', 'r') as f:
            for linea in f:
                if linea != '\n':
                    lista.append(int(linea.rstrip()))
                    
                else:
                    suma = sum(lista)
                    lista_sumas.append(suma)
                    lista.clear()
                    suma = 0

        maximo = 0
        for i in range(3):
            for n in lista_sumas:    
                if(n > maximo):
                    maximo = n
            elfos_mas_calorias.append(maximo)
            lista_sumas.remove(maximo)
            maximo = 0

        return sum(elfos_mas_calorias)

