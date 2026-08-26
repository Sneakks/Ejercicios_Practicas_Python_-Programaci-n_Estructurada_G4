import os

def creditoInterno():
    os.system("cls")

    registro = input("¿Eres una persona registrada? (Si/No)")
    print("AVISO: NOSOTROS VENDEMOS A CRÉDITOS ÚNICAMENTE A USUARIOS REGISTRADOS")

    if registro.lower() == "si":
        saldo = float(input ("Ingrese su saldo actual C$: "))
        if saldo <= 500:
            print("Crédito disponible")
        else: print("Por favor regularice el saldo")
    else:
        print("Compra realizada de contado")
