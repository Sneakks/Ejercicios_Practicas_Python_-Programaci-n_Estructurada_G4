import os

def produccionPan():
    os.system("cls")

    registro = []

    for i in range(1, 7):
        try:
            produccion = int(input(f"Ingrese la cantidad de pan producido en el día {i}: "))
            vent = int(input(f"Ingrese la cantidad de pan vendido en el día {i}: "))
        except ValueError:
            print("Ingrese solamente números enteros en ambas preguntas")
            return

        registro.append((produccion, vent))

    print("*** Sobrante por día ***")
    totalProduccion = 0
    totalVentas = 0
    dia = 1

    for produccion, vent in registro:
        sobrante = produccion - vent
        print(f"Día {dia}: produjo {produccion}, vendió {vent}, sobrante = {sobrante}")

        totalProduccion += produccion
        totalVentas += vent
        dia += 1

    sobranteTotal = totalProduccion - totalVentas

    print(f"Total producido en la semana: {totalProduccion}")
    print(f"Total vendido en la semana: {totalVentas}")
    print(f"Sobrante total de la semana: {sobranteTotal}")






