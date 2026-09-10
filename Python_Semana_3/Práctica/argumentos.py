import os

def imprimirDatos(cif, nombre, promedio, becado):
    if (promedio >= 80) and (becado == True):
        estatus = "Renovado"
    elif(promedio < 80) and (becado == True):
        estatus = "Revocado"
    else:
        estatus = "No becado"

    os.system("cls")
    print("Datos del estudiante")
    print("*"* 15)
    print(f"CIF: {cif}")
    print(f"Nombre: {nombre}")
    print(f"Promedio: {promedio}")
    print(f"Estado de beca: {estatus}")
    print("*"*15)

def leerDatos():
    print("//////// Registro de Estudiantes ////////")
    cif = input("Ingrese el cif del estudiante: ")
    nombre = input("Ingrese el nombre completo del estudiante: ")
    promedio = float(input("Ingrese el promedio del estudiante: "))
    beca = input("¿El estudiante es becado? S/N: ")
    if(beca.strip().upper() =="S"):
        becado = True
    else:
        becado = False
    return cif, nombre,promedio,becado