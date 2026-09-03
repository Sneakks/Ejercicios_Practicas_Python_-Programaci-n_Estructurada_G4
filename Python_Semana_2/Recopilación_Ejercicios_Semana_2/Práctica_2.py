import os
os.system("cls")

registrado = input ("¿Cliente registrado?")

if registrado.lower() == "si":
    saldo = float(input("Saldo C$: "))
    if saldo <=500:
        print("Crédito disponible")
    else:
        print("Regularice el estado")
else:
    print("Compra de contado")
