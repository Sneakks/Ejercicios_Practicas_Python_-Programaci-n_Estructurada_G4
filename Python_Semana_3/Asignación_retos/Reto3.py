import os

def calcular_tarifa(distancia, zona):
    if zona.lower() == "urbana":
        tarifa_base = 20
        costo_km = 5
    elif zona.lower() == "rural":
        tarifa_base = 35
        costo_km = 8
    else:
        return None

    tarifa = tarifa_base + (distancia * costo_km)
    return tarifa


def main():
    os.system("cls")
    distancia = float(input("Digite la distancia en km: "))
    zona = input("Digite la zona (urbana/rural): ")

    tarifa = calcular_tarifa(distancia, zona)

    if tarifa is None:
        print("Zona no reconocida.")
    else:
        print(f"Tarifa de entrega: C$ {tarifa:.2f}")

main()