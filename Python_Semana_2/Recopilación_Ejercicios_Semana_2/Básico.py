import os

def main ():
    os.system("cls")
    #La variable es un str que queda de la siguiente manera; nombreAsignatura (Camel Case)
    nombreAsignatura = input("Ingrese el nombre de la asignatura")

    #La variables activa es de tipo bool
    respuesta = input("¿La asignatura esta activa? (s/n): ").strip().lower()
    activa = respuesta in ["s","si","ture","1" ]

    #La variable nota es de tipo float 
    nota = float(input("Digite la nota obtenida: "))

    #La variable numeroDeCreditos es de tipo int
    numeroDeCreditos = int(input("Ingrese el número de créditos obtenido: "))
    
    #Limpiar terminal
    os.system("cls")
    
    
    print("****************************************************************")

    #Ahora imprimirmos todos los valores

    print(f"Nombre de la asignatura: {nombreAsignatura}")
    print(f"La asignatura esta: {activa}")
    print(f"La nota obtenida es de: {nota}")
    print(f"El número de créditos es de: {numeroDeCreditos}")
main()
