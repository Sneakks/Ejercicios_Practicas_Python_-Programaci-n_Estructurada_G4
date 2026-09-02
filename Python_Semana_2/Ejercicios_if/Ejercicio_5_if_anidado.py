import os

def ventaFerreteria():
    print("Bienvenido a la ferretería FerroMax")

    try:
        client = input("Ingrese el tipo de cliente que es usted: (Mayorista) o (Minorista) ")
    except ValueError:
        print("Por favor solo ingrese palabras, nada de números)")
        return

    try:
        tipo = int(input("Ingrese el monto de dinero invertido: "))
    except ValueError:
        print("Por favor solo ingrese el monto en números enteros ")
        return


    if client.lower() == "mayorista":
        if tipo >= 5000:
            print("Felicidades ha obtenido un descuento del 20% en su compra final.")
    else:
        print("Agradecemos mucho su compra, sin embargo usted necesita una compra superior a C$ 5,000 para aplicar a un descuento especial.")

    if client.lower() == "minorista":
        if tipo >= 1000:
            print("Felicidades ha obtenido un descuento del 10% en su compra final.")
    else:
        print("Agradecemos mucho su compra sin embargo usted necesita de una compra superior a los C$ 1000 para aplicar a un descuento espeial")
