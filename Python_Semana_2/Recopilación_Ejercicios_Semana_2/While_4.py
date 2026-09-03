import os

def combustibleReparto():
    os.system("cls")

    combustible = 8
    recorrido = 1

    print(f"La motocicleta inicia con {combustible} litros de combustible")

    while combustible > 0:
        consumo = float(input(f"Ingrese el consumo del recorrido #{recorrido} (litros): "))
        combustible -= consumo

        if combustible <= 0:
            print("¡Combustible agotado! No es posible continuar con más recorridos")
        elif combustible <= 1:
            print(f" Alerta: queda poco combustible ({combustible} litros)")
        else:
            print(f"Combustible restante: {combustible} litros")

        recorrido += 1

    print(f"Se registraron {recorrido - 1} recorridos en total")