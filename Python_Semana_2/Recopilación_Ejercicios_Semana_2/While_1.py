import os
def cierreCaja():
    os.system("cls")

    total = 0
    cantidadVentas = 0

    monto = float(input("Ingrese el monto de la venta (Ingrese 0 para terminar)"))

    while monto != 0:
        total += monto
        cantidadVentas += 1
        monto = float(input("Ingrese el monto de la venta (Ingrese 0 para terminar): "))

        print(f"Total recaudado: {total}")
        print(f"Cantidad de ventas registradas {cantidadVentas}")

