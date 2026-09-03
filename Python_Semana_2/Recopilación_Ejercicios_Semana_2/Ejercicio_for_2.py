import os
def recepciónCafe():
    os.system("cls")

    cafe = []

    for i in range(1, 6):
        try:
            saco = int(input(f"Ingrese cuanto pesa el saco # {i}: "))
        except ValueError:
            print("Por favor ingrese solamente números enteros")
            return

        cafe.append(saco)
        print(f"Saco #{i} recibido con un peso de {saco} kg")

    total = sum(cafe)
    print(f"El peso total de los 5 sacos ingresados es de: {total} kg")

