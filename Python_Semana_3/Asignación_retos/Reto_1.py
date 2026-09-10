import os


def calcular_comision(ventas, porcentaje):
    comision = ventas * porcentaje/100
    return comision


def main():
    os.system("cls")
    ventas = float(input("Digite el monto de ventas: "))
    porcentaje = int(input("Digite el porcentaje de comisión (número entero): "))
    comision = calcular_comision(ventas, porcentaje)
    print(f"La comisión del vendedor es: C$ {comision:.2f}")

main()