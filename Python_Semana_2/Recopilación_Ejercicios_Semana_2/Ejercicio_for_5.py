import os
def evaluacionServicio():
    os.system("cls")
    calificaciones = []

    for i in range (1, 11):
        try:
            cali = int(input("Ingrese una calificación del 1 - 5 su satisfacción del servicio: "))
        except ValueError:
            print("Por favor solo ingrese números enteros")
            return

        calificaciones.append(cali)
        print("Promedio de Calificaciones: ")

        promedio = sum(calificaciones) / len(calificaciones)

        altas = 0 

        for cali in calificaciones: 
            if cali == 4 or 5: 
                altas += 1
        print(f"El promedio de calificaciones es: {promedio}")
        print(f"La cantidad de calificaciones entre 4 o 5: {altas}")