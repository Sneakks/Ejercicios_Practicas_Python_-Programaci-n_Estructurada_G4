import os

def servicioEntrega():
    os.system("cls")
    peso = float(input("Ingrese el peso exacto de su producto"))
    print("AVISO: APLICAMOS TARIFAS POR ZONAS (MANAGUA Y CHONTALES)")
    print("Managua : Zona Rural = C$ 100, Zona urbana = C$ 50")
    print("Estelí : Zona Rural = C$ 200, Zona urbana = C$ 100")


    zone = input("Ingrese la zona a la que se va a hacer la entrega: ")

    tarifaRuralManagua = 100
    tarifaUrbanaManagua = 50

    tarifaRuralEsteli = 200
    tarifaUrbanaEsteli = 100

    if peso > 5 :
        print("Su producto supera el peso definido, se le va a cobrar una tarifa extra dependiendo su municipio")
        muni = input("Ingrese el municipio de entrega: ")
        if muni.lower() == "managua":
            print("Se le va a cobrar uan tarifa extra dependiendo su zona")
            zone = input("Ingrese la zona a la que se va a hacer la entrega: ")
            if zone.lower() == "rural":
                print("La tarifa que se le va a cobrar es de aproximadamente C$ 100")
            elif zone.lower() == "urbana":
                print("La tarifa que se le va a aplicar es de aproximadamente C$ 50")
            elif muni.lower() == "chontales":
                print("Se le va a cobrar una tarifa dependiendo de su zona")
                input("Ingrese la zona en que se le va a hacer la entrega: ")
            elif zone == "rural":
                print("Se le va a cobrar una tarifa de C$ 200")
            elif zone == "urbana":
                print ("Se le va a cobrar una tarifa de C$ 100")
    else:
        print("No se le aplicara ninguna tarifa extra")









