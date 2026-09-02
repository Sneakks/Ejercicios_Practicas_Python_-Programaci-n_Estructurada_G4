import os
def ventasMinisuper():
    os.system("cls")
    ventasDia1 = ventasDia2 = ventasDia3 = ventasDia4 = ventasDia5 = ventasDia6 = ventasDia7 = 0
    for i in range(1,8): #Controla los días de la semana
        for j in range(1,4): #Controla las ventas del día
            venta = float(input(f"Ingrese la venta {j}, del día {i}"))
            match i:
                case 1:
                        ventasDia1 += venta
                case 2:
                        ventasDia2 += venta
                case 3:
                        ventasDia3 += venta
                case 4:
                        ventasDia4 += venta
                case 5:
                        ventasDia5 += venta
                case 6:
                        ventasDia6 += venta
                case 7:
                        ventasDia7 += venta

    ventasSem = ventasDia1 +ventasDia2 + ventasDia3 + ventasDia4 + ventasDia5 + ventasDia6 + ventasDia7  

    print("La venta total de la semana es: C$",ventasSem)
    print(f"El promedio de ventas del día 1 es: C$ {ventasDia1/3}")
    print(f"El promedio de ventas del día 2 es: C$ {ventasDia2/3}")
    print(f"El promedio de ventas del día 3 es: C$ {ventasDia3/3}")
    print(f"El promedio de ventas del día 4 es: C$ {ventasDia4/3}")
    print(f"El promedio de ventas del día 5 es: C$ {ventasDia5/3}")
    print(f"El promedio de ventas del día 6 es: C$ {ventasDia6/3}")
    print(f"El promedio de ventas del día 7 es: C$ {ventasDia7/3}")

ventasMinisuper()

