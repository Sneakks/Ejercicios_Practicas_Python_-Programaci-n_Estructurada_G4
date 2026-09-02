import os
from Situación_1 import inventarioPulperia
from Situación_2 import promocionTienda
from Situación_3 import metaVentas
from Situación_4 import entregaComedor
from Situación_5 import pesoProductos
from Ejercicio_1_if_anidado import creditoInterno
from Ejercicio_2_if_anidado import servicioEntrega
from Ejercicio_3_if_anidado import clasificaciónCafe
from Ejercicio_4_if_anidado import reservaHospedaje
from Ejercicio_5_if_anidado import ventaFerreteria

def main():
    opc = 0
    while opc != 11:
        os.system("cls")
        print("******* Menú de funciones *********")
        print("1 - Inventario de pulpería")
        print("2 - Promoción de una tienda")
        print("3 - Meta de Ventas")
        print("4 - Entrega de un comedor")
        print("5 - Peso productos")
        print("6 - Credito Interno")
        print("7 - Servicio de Entrega")
        print("8 - Clasificación de café")
        print("9 - Reserva de hospedaje")
        print("10 - Venta de ferretería")
        print("11 - Salir del programa")
        print("-"*40)
        
        try:
            opc = int(input("Selccione una opción: "))
        except ValueError:
            print("Por favor solo ingrese números enteros que se encuentren dentro del menú.")
            os.system("pause")
            continue
        print("-"*30)
        #Invocar una función según opción menú seleccionada
        match opc:
            case 1:
                inventarioPulperia()
            case 2: 
                promocionTienda()
            case 3:
                metaVentas()
            case 4:
                entregaComedor()
            case 5:
                pesoProductos()
            case 6:
                creditoInterno()
            case 7:
                servicioEntrega()
            case 8:
                clasificaciónCafe()
            case 9:
                reservaHospedaje()
            case 10:
                ventaFerreteria()
            case 11:
                    print("Adiós, hasta pronto")
            case _:
                    print("Opción incorrecta")
        if opc != 11:
            os.system("pause")
main()