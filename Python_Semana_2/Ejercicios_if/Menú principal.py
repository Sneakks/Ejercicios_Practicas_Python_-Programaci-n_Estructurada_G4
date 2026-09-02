import os
from Situación_1 import inventarioPulperia
from Situación_2 import promocionTienda
from Situación_3 import metaVentas
from Situación_4 import entregaComedor
from Situación_5 import pesoProductos
from Ejercicio_1_if_anidado import  creditoInterno

def main ( ):
    os.system("cls")
    while True:
        print("*******************************")
        print("Menú Principal / Ejercicios S2")
        print("*******************************")
        print("1. Inventario Pulperería")
        print("2. Promoción de una tienda")
        print("3. Meta de ventas")
        print("4. Entrega de un comedor")
        print("5. Peso de productos")
        print("11. Salir del menú")
        print("*******************************")
        opcion = input("Digite la opción de su preferencia: ")

        if opcion == "1":
            inventarioPulperia()
            input("Ingrese enter para volver al menú")
        elif opcion == "2":
            promocionTienda()
            input("Ingrese enter para volver al menú")
        elif opcion == "3":
            metaVentas()
            input("Ingrese enter para volver al menú")
        elif opcion == "4":
            entregaComedor()
            input("Ingrese enter para volver al menú")
        elif opcion == "5":
            pesoProductos()
            input("Ingrese enter para volver al menú")
        elif opcion == "6":
            creditoInterno()
        elif opcion == "11":
            print("*****************************************")
            print("Muchas gracias por utilizar el programa")
            print("*****************************************")
            break
        else: 
            print("Opción inválida, ingrese por favor entre las opciones disponibles: 1 - 6")
            input("Ingrese enter para regresar al menú: ")

main()