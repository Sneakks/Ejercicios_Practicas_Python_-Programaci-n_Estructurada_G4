import os
def inventarioPulperia():
    os.system("cls")
    nombreProducto = input("Ingrese el nombre del producto: ")
    unidadExistente = int(input("Ingrese la cantidad de unidades existentes: "))

    if unidadExistente >= 5 :
        print("Todavía no se requiere comprar más", nombreProducto)
    else:
        print("Se requiere rellenar el producto con urgencia")

