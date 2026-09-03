import os
def promocionTienda():
    os.system("cls")
    descuento = float(input("Bienvenido a *****SUPER DESCUENTOS*****, porfavor ingrese el monto total de su compra: "))

    if descuento > 1500:
        final = descuento - descuento * 0.10
        print ("El descuento aplicado fue de un 10%, precio original: ",descuento, "precio con descuento aplicado: ", final)
    else: 
        print("Este monto es insuficiente para obtener un descuento, monto ingresado:",descuento, " Los descuentos solo aplican a compras superiores a C$ 1,500")