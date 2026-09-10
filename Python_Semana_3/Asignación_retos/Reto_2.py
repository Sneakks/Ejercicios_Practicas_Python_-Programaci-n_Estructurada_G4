import os

def clasificar_cafe(humedad):
    if 10 <= humedad <= 12:
        return "aceptado"
    else:
        return "revisar"


def main():
    os.system("cls")
    humedad = float(input("Digite el porcentaje de humedad del café: "))
    resultado = clasificar_cafe(humedad)
    print(f"Clasificación: {resultado}")

main()