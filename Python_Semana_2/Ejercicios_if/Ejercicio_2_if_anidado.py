import os

def servicioEntrega():
    os.system("cls")

    zona = input("Ingrese la zona en la que se encuentra (Rural o Urbana: )")
    print("Estos son los precios que se cobran dependiendo de su zona y si cumple la métrica estricta de 5kg: (Zona rural = C$100, Zona urbana = C$ 50)")
    cargorural = 100
    cargourbano = 50
    recargo = 100

    if zona.lower() == "urbana":
        try:
            peso = int(input("Ingrese el peso del producto: "))
        except ValueError:
            print("Valores erróneos, por favor solo ingrese números enteros.")
            return

        if peso > 5:
            print("Su entrega tiene un recargo de C$ 100 extra su saldo final es: ", cargourbano + recargo )
        else:
            print("El precio a cancelar de su entrega final es de: C$", cargourbano, )

    elif zona.lower() == "rural":
        try:
            peso = int(input("Ingrese el peso del producto que desea ser entregado a usted: "))
        except ValueError:
            print("Valores erróneos, por favor solo ingrese números enteros.")
            return
        
        if peso > 5:
            print("Su entrega tiene un recargo de C$ 100 extra su saldo final es: ", cargorural + recargo )
        else:
            print("El precio a cancelar de su entrega final es de: C$", cargorural )
    else: 
        print("Zona no reconocida, por favor solo ingrese Rural o Urbana")