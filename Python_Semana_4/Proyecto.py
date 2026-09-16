import os

def leerTexto(mensaje):

    while True:
        entrada = input(mensaje).strip()## .strip() funciona como limpiadro de espacios inecesarios realizados por el usuario
        if not entrada:
            print("Este campo no puede quedar vacío, ingrese texto válido por favor")
        elif entrada.isdigit():
            print("Los números deben ir acompañados de texto, no puedes ingresar solo números")
        else:
            return entrada

def leerNumero(mensaje):

    while True:
        entrada = input(mensaje).strip()
        if not entrada:
            print("Este espacio no puede quedar en blanco, ingrese solo números por favor ")
            continue
        try:
            valor = float(entrada)
            if valor < 0:
                print("El monto no puede ser uno negativo, ingrese únicamente valores positivos")
            else:
                return valor
        except ValueError:
            print("Por favor ingrese valóres númericos")


def ingresarDatos():

    print("*"*40)
    print("      REGISTRO DE DATOS FINANCIEROS           ")
    print("*"*40)
    
    nombre = leerTexto("Ingresa tu nombre: ")
    ingresos = leerNumero("Ingresos totales del mes ($): ")
    gastos = leerNumero("Gastos totales del mes ($): ")
    meta_ahorro = leerNumero("Meta de ahorro para este mes ($): ")
    
    return nombre, ingresos, gastos, meta_ahorro

def calcularBalance(ingresos, gastos):
    return ingresos - gastos

def evaluarAhorro(balance, meta_ahorro):
    if balance >= meta_ahorro:
        sobrante = balance - meta_ahorro
        return f"¡Felicidades! Lograste tu meta y te sobraron ${sobrante:,.2f} adicionales."##Devolvemos de una sola vez la frase dentro de la línea return sin necesidad de ocupar un print previo
    else:
        faltante = meta_ahorro - balance
        return f"No alcanzaste la meta. Te faltaron ${faltante:,.2f}."

def mostrarResumen(nombre, ingresos, gastos, balance, estado_ahorro):
    os.system("cls")
    print("*"*40)
    print(f"    RESUMEN FINANCIERO MENSUAL DE {nombre.upper()}")
    print("*"*40)
    print(f" Ingresos Totales : ${ingresos:,.2f}")
    print(f" Gastos Totales   : ${gastos:,.2f}")
    print("*"*40)
    print(f" Balance Disponible: ${balance:,.2f}")
    print(f" Estado de Ahorro  : {estado_ahorro}")
print("*"*40)



def main():
    os.system("cls")
    nombre, ingresos, gastos, meta = ingresarDatos()
    balance = calcularBalance(ingresos, gastos)
    estado = evaluarAhorro(balance, meta)
    
    mostrarResumen(nombre, ingresos, gastos, balance, estado)


main()