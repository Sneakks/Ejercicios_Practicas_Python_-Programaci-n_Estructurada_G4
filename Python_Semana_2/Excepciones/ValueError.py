
def convertirEdad():
    try:
        edad = int(input("Digite su edad: "))
    except ValueError:
        print("Debe ingresar un valor entero.")
    else:
        print("Edad registrada exitósamente: ",edad)