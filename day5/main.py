def RellenarPilas():
    with open("/home/juanjo/adventofcode/day5/input.txt", "r") as f:
        texto = f.read().splitlines()

    stack_list = [[] for _ in range(9)]

    pilas_leidas = True

    for linea in texto:
            
        if len(linea) == 0:
            pilas_leidas = False
            for i in range(len(stack_list)):
                stack_list[i] = stack_list[i][::-1][1:]
        else:
            if pilas_leidas:
                pila = 0
                for i in range(1, len(linea), 4):
                        
                    if linea[i] != " ":
                        stack_list[pila].append(linea[i])
                    pila += 1
            else:
                num_elementos = int(linea.split(" ")[1])
                origen = int(linea.split(" ")[3]) - 1
                destino = int(linea.split(" ")[5]) - 1
                #problema1
                #stack_list[destino] = stack_list[destino] + stack_list[origen][-num_elementos:][::-1]
                #problema2
                stack_list[destino] = stack_list[destino] + stack_list[origen][-num_elementos:]
                stack_list[origen] = stack_list[origen][:-num_elementos]
    return stack_list

def main():
    carga = RellenarPilas()
    print(carga)
    ultimas_cajas = []
    for pila in carga:
        ultimas_cajas.append(pila[-1])
    print(ultimas_cajas)

if __name__ == '__main__':
    main()
    
    

