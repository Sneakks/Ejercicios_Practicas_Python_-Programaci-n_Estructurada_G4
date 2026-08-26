import os
def metaVentas():
    os.system("cls")
    totalVendido = float(input("Ingrese el monto total vendido: "))
    print("Meta Diaria de venta: Superior a los C$ 4,000")

    if totalVendido > 4000:
        print ("¡Felicidades, has superado la meta diaria de venta!")
        print ("Tu venta es de alrededor de: ", totalVendido)
    else:
        print("¡Enhorabuena por tu venta!, sin embargo aún no has superado la meta diaria")
        print("Tu venta actual es de: ", totalVendido)