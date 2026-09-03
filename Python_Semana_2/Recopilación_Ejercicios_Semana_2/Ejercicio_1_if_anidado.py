import os

def creditoInterno():
    os.system("cls")  
    registro = input("¿Cliente registrado? (Si/No) ")

    if registro.lower() == "si":
        try:
            saldo = float(input("Saldo C$: "))
        except ValueError:
            print("Saldo inválido, ingrese solo números")
            return
        if saldo <= 500:
            print("Crédito disponible")
        else:
            print("Regularice el saldo")
    else:
        print("Compra de contado")
