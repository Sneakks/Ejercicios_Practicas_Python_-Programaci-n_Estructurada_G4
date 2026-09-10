import os

def main():
    #Inicialización de Variables
    mensaje = "¡Bienvenido a la Tienda Vale Todo!"
    nombre = None
    precio = 0.0
    cantidad = 0
    porcentaje = 0.0
    impuesto = 0.15
    total = subtotal = descuento = iva = 0.0

    #Invocación a leer nombre
    nombre = leer_nombre(mensaje)

    #Lectura de datos con validación
    precio = leer_numero("Digite el precio del artículo: ")
    cantidad = int(leer_numero("¿Cuántas unidades va a comprar?: "))
    porcentaje = leer_numero("Digite el porcentaje de descuento: ")

    #Invocación a calcular_total
    total,subtotal,descuento,iva = calcular_total(precio,cantidad,porcentaje,impuesto)

    mostrar_factura(nombre,precio,cantidad,porcentaje,impuesto,total,subtotal,descuento,iva)

def leer_numero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            numero = float(entrada)
            if numero < 0:
                print("El valor no puede ser negativo. Intente de nuevo.")
                continue
            return numero
        except ValueError:
            print("Debe digitar un número válido. Intente de nuevo.")

def leer_nombre(mensaje):
    os.system("cls")
    print(mensaje)
    print("*"* 40)
    nombre = input("Digite el nombre del cliente: ")
    return nombre

def calcular_total(precio,cantidad,porcentaje,impuesto):
    subtotal = calcular_subtotal(precio,cantidad)
    descuento = calcular_descuento(subtotal,porcentaje)
    iva = (subtotal-descuento) * impuesto
    total = (subtotal-descuento) + iva
    return total,subtotal,descuento,iva

def calcular_subtotal(precio,cantidad):
    subtotal = precio * cantidad
    return subtotal

def calcular_descuento(subtotal,porcentaje):
    descuento = subtotal * porcentaje
    return descuento

def mostrar_factura(nombre,precio,cantidad,porcentaje,impuesto,total,subtotal,descuento,iva):
    print("*"*40)
    print("        FACTURA - TIENDA VALE TODO")
    print("*"*40)
    print(f"Cliente: {nombre}")
    print(f"Precio unitario: C$ {precio:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: C$ {subtotal:.2f}")
    print(f"Descuento ({porcentaje*100:.0f}%): C$ {descuento:.2f}")
    print(f"IVA ({impuesto*100:.0f}%): C$ {iva:.2f}")
    print("-"*40)
    print(f"TOTAL A PAGAR: C$ {total:.2f}")
    print("*"*40)

main()