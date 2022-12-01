class Test1:
    def __init__(self):
        self.elfs = []

    def rellenar_datos(self):
        with open('/home/juanjo/adventofcode/reto1/input.txt', 'r') as f:
            lista = []
            for linea in f:
                if linea != '\n':
                    lista.append(linea)
                
                else:
                    self.elfs.append(lista)
                    lista.clear()

    def Elfs(self):
        return self.elfs

    def obtener_mayor_calorias(self):
        maximo = 0
        suma = 0

        for lista in self.elfs:
            
            for l in lista: 
                suma += int(l)

            if maximo < suma:
                maximo = suma
            suma = 0

        return maximo