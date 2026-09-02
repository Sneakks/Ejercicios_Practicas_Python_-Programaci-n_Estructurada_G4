from Situación_1 import creditoInterno
from Situación_2 import servicioEntrega


def main ( ):
    while True:
        print("*******************************")
        print("Menú Principal / Ejercicios S2")
        print("*******************************")
        print("1. Crédito Interno")
        print("2. Servicio de entrega")
        print("3. Clasificación de café")
        print("4. Reserva de hospedaje")
        print("5. Venta de ferretería")
        print("6. Salir del menú")
        print("*******************************")
        opcion = input("Digite la opción de su preferencia: ")

        if opcion == "1":
            creditoInterno()
            input("Ingrese enter para volver al menú")
        elif opcion == "2":
            servicioEntrega()
            input("Ingrese enter para volver al menú")
        elif opcion == "3":
            
            input("Ingrese enter para volver al menú")
        elif opcion == "4":
            
            input("Ingrese enter para volver al menú")
        elif opcion == "5":
            
            input("Ingrese enter para volver al menú")
        elif opcion == "6":
            print("*****************************************")
            print("Muchas gracias por utilizar el programa")
            print("*****************************************")
            break
        else: 
            print("Opción inválida, ingrese por favor entre las opciones disponibles: 1 - 6")
            input("Ingrese enter para regresar al menú: ")

main()