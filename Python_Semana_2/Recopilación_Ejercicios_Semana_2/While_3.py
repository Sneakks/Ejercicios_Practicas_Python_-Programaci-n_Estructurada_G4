import os

def pedidoDistribuidor():
    os.system("cls")

    precioUnitario = 25 

    cantidad = int(input("Ingrese la cantidad de unidades a pedir (1 - 100): "))

    while cantidad < 1 or cantidad > 100:
        print("Cantidad inválida, debe estar entre 1 y 100")
        cantidad = int(input("Ingrese la cantidad de unidades a pedir (1 - 100): "))

    total = cantidad * precioUnitario

    print(f"Cantidad pedida: {cantidad} unidades")
    print(f"Precio unitario: C${precioUnitario}")
    print(f"Total a pagar: C${total}")


