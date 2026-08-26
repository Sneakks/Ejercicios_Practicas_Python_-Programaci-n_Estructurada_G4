import os 

def pesoProductos():
    os.system("cls")
    print("*********************************")
    print("Bienvenido a la báscula de sacos")
    print("*********************************")

    pes = int(input("Ingrese el peso del saco a consultar: "))

    print("AVISO: EL SACO TIENE QUE PESAR 46 KG EXACTOS O MÁS PARA CUMPLIR CON LOS REQUISITOS")

    if pes <= 46:
        print("El saco cumple con las normativas de peso")
    else:
        print("El saco no cumple con las normativas de pesaje y tiene que ser inspeccionado para cumplir con la normativa de 46 KG")
