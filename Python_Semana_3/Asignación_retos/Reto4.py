import os

def resumen_ventas(ventas):
    total = sum(ventas)
    promedio = total / len(ventas)
    minima = min(ventas)
    maxima = max(ventas)
    return total, promedio, minima, maxima


def main():
    os.system("cls")
    ventas = []
    for dia in range(1, 8):
        venta = float(input(f"Digite la venta del día {dia}: "))
        ventas.append(venta)

    total, promedio, minima, maxima = resumen_ventas(ventas)

    print(f"Total de la semana: C$ {total:.2f}")
    print(f"Promedio diario: C$ {promedio:.2f}")
    print(f"Venta mínima: C$ {minima:.2f}")
    print(f"Venta máxima: C$ {maxima:.2f}")

main()