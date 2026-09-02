def dividirSeguro():
    try:
        a = float(input("Dividiendo: "))
        b = float(input("Divisor: "))
        resultado = a/b
    except ValueError:
        print("Ingrese valores numéricos.")
    except ZeroDivisionError:
        print("El divisor no puede ser cero: ")
    else:
        print("Resultad: ", resultado)