import os

def reposicionExistencias():
    os.system("cls")

    existencias = 3
    meta = 20
    reposicion = 1

    print(f"La tienda inicia con {existencias} unidades. Meta: {meta} unidades")

    while existencias < meta:
        cantidad = int(input(f"Ingrese la cantidad repuesta #{reposicion}: "))
        existencias += cantidad

        print(f"Existencias actuales: {existencias} unidades")

        reposicion += 1

    print(f"¡Meta alcanzada! Existencias finales: {existencias} unidades")
    print(f"Se realizaron {reposicion - 1} reposiciones")

