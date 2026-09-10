#parámetros inmutables
import os

def aumentar(numero):
    numero = numero + 1
    print(f"numero = {numero}")
    return numero

os.system("cls")
cantidad = 5
cantidad = aumentar(cantidad)
print(f"cantidad = {cantidad}")
