import os
def recepcionInventario():
    os.system("cls")

    productos = [] 

    for i in range(1, 9):
        try:
            nombre = input(f"Ingrese el nombre del árticulo # {i} ")
            existencia = int(input(f"Ingrese la cantidad de existencias del producto # {i}"))
        except ValueError:
            print("Valores inválidos, por favor ingrese letras en la primera pregunta y números enteros en la segunda")
            return

        productos.append ((nombre, existencia)) 

        print("Productos con existencias menores a 10 unidades: ")

        alertas = 0

    for nombre, existencia in productos:
        if existencia < 10:
            print(f" Alerta: {nombre} tiene solo {existencia} unidades")
            alertas +=1
    print(f"Total de alertas encontradas {alertas}")
