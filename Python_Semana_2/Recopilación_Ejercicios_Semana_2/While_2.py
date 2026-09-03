import os
def accesoSistema():
    os.system("cls")

    contraseña = str("micasa")
    fallo = 0


    intentos = input("Ingrese la contraseña: ")
    while intento != contraseña:
        intento = input("Contraseña incorrecta, intente de nuevo: ")
        intentos += 1

        print(f"Acceso concedido, Se necesitaron {intento} para ingresar la contraseña correctamente")

