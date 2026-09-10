import os

def calcular_nota_final(nota1, nota2, nota3, peso1, peso2, peso3):
    nota_final = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
    return nota_final


def clasificar_nota(nota_final):
    if nota_final >= 90:
        return "Excelente"
    elif nota_final >= 70:
        return "Aprobado"
    else:
        return "Reprobado"


def main():
    os.system("cls")
    nota1 = float(input("Digite la primera nota: "))
    nota2 = float(input("Digite la segunda nota: "))
    nota3 = float(input("Digite la tercera nota: "))

    peso1 = float(input("Digite la ponderación de la primera nota (ej. 0.3): "))
    peso2 = float(input("Digite la ponderación de la segunda nota: "))
    peso3 = float(input("Digite la ponderación de la tercera nota: "))

    nota_final = calcular_nota_final(nota1, nota2, nota3, peso1, peso2, peso3)
    clasificacion = clasificar_nota(nota_final)

    print(f"Nota final: {nota_final:.2f}")
    print(f"Clasificación: {clasificacion}")

main()