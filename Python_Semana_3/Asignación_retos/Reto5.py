import os

def productos_a_reponer(existencias, limite):
    reponer = []
    for producto, cantidad in existencias.items():
        if cantidad < limite:
            reponer.append(producto)
    return reponer


def main():
    os.system("cls")
    existencias = {
        "Arroz": 15,
        "Azúcar": 5,
        "Aceite": 8,
        "Frijoles": 20,
    }
    limite = int(input("Digite el límite mínimo de existencias: "))

    productos = productos_a_reponer(existencias, limite)

    if productos:
        print("Productos que deben reponerse:")
        for p in productos:
            print(f"- {p}")
    else:
        print("No hay productos por reponer.")

main()