import os

def clasificaciónCafe():
    os.system("cls")

    print("Bienvenido al verificador de húmedad")
    print("Primero se verificara que la humedad de café se encuentre entre 10% y 12%")
    print("En el dado caso que cumpla, se clasificara dependiendo de los defectos que sean reportados: ")
    print(" - 0 a 5 defectos = Categoría Primera")
    print(" - 6 a 15 defectos = Categoría Segunda")
    print(" - Más de 15 defectos = Categoría Rechazo")

    try:
        humedad = int(input("Ingrese el porcentaje de la humedad del lote: "))
    except ValueError:
        print("Por favor solo ingrese números enteros")
        return 
    if 10 <= humedad <= 12:
        try:
            defectos = int(input("Ingrese la cantidad de defectos reportados: "))
        except ValueError:
            print("Por favor ingrese la cantidad de defectos en números enteros.")
            return
        if defectos <= 5:
            print("El lote se clasifica como Categoría Primera")
        elif defectos <= 15:
            print("El lote se clasifica como Categoría Segunda")
        else:
            print("El lote se clasifica como Categoría Rechazo")
    else:
        print("El lote no cumple con el rango de humedad requerido (10% - 12%)")
