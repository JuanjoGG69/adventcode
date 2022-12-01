from elfos.elfos import Test1

def main():
     
    calorias = Test1()
    calorias.rellenar_datos()
    print(calorias.obtener_mayor_calorias())

if __name__ == '__main__':
    main()