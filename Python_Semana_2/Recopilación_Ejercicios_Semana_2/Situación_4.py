import os 

def entregaComedor():
    os.system("cls")
    print("####################")
    print("Bienvenido al Chante")
    print("####################")

    pago = float(input("Ingrese el monto de su entrega: "))
    print("AVISO : APLICAMOS RECARGA DE C$ 40 SI SU ENTREGA SUPERA LOS C$300")

    if pago <= 300:
        print("El monto ingresado es de: ",pago, "su entrega es totalmente gratuita")
    else:
        reca = pago + 40
        print("El monto ingresado es de: ", pago, "sin embargo se le aplicara una recarga de C$ 40")
        print("Precio final de su entrega: ",reca)