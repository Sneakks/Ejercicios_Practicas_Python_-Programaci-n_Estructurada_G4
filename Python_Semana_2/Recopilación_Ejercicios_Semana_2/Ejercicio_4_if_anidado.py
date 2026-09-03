import os

def reservaHospedaje():
    os.system("cls")
    print("Bienvenido al Hotel Granadita")

    tempo = input("Ingrese en que temporada del año se encuentra (Baja/Alta): ")
    try:
        reser = int(input("Por favor ingrese la cantidad de noches que va a estar con nosotros: "))
    except ValueError:
        print("Por favor ingrese solamente número enteros para especificar la cantidad de noches")
        return

    print("ANUNCIO IMPORTANTE: Brindamos un porcentaje de descuento especial solo para reservas de tres noches durante temporadas bajas")

    if tempo.lower() == "baja":
        if reser >= 3:
            print("Felicidades ha obtenido un descuento único por su reserva de 3 noches, este equivale a un 15% de descuento en su compra final")
        else:
            print("Por el momento si se encuentra en temporada baja pero necesita tener una reserva mínima de tres noches para aplicar ael descuento expecial.")
    elif tempo.lower() == "alta":
        print("Por el momento no aplcamos descuentos especiales durante temporadas altas")
    else:
        print("Por favor solo ingrese las palabras baja o alta para dar a entender la temporada en la que s eencuentra")