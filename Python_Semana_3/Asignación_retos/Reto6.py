import os

def leer_monto():
    while True:
        entrada = input("Digite el monto en dólares: ")
        try:
            monto = float(entrada)
            return monto
        except ValueError:
            print("Debe digitar un número válido.")


def validar_monto(monto):
    return monto >= 0


def convertir_a_cordobas(monto, tasa_cambio):
    return monto * tasa_cambio


def presentar_conversion(monto_dolares, monto_cordobas, tasa_cambio):
    print("*" * 30)
    print(f"Monto en dólares: $ {monto_dolares:.2f}")
    print(f"Tasa de cambio: {tasa_cambio:.2f}")
    print(f"Monto en córdobas: C$ {monto_cordobas:.2f}")
    print("*" * 30)


def main():
    os.system("cls")
    tasa_cambio = 36.6

    monto_dolares = leer_monto()

    if not validar_monto(monto_dolares):
        print("El monto no puede ser negativo.")
        return

    monto_cordobas = convertir_a_cordobas(monto_dolares, tasa_cambio)
    presentar_conversion(monto_dolares, monto_cordobas, tasa_cambio)

main()