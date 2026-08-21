import keyword
import os

os. system("cls")
#Lista de palabras reservadas de Python
print ("LISTA DE PALABRAS RESERVADAS DE PYTHON")
print(keyword.kwlist)
print("*******************************************************")
# Verifica si un token es una palabra reservada o no 
print("¿while es una palabra reservada? Respuesta = " + str(keyword.iskeyword("While")))

print("¿estudiante es una palabra reservada? Respuesta = "+ str(keyword.iskeyword("estudiante")))

print("///////////////////////////////////////////")

X = 8
Y = 3
Z = X/Y
print(f"{Z:.2f}")

print(f"{X} dividido entre Y es equivalente a {Z:0.2f}")

var = int(input("Digite un valor entero "))
answer = var >= Y and var <= X
print(f"¿El valor leido es {var}, esta entre {X} y {Y}? Respuesta = {answer}")