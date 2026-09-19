import os

def leer_numero(mensaje):

    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo. Ingrese únicamente números positivos")
                continue
            return valor
        except ValueError:
            print("Debe digitar un número válido. Intentelo de nuevo")


def leer_nombre(mensaje):
    os.system("cls")
    print(mensaje)
    print("*"*40)
    nombre = input("Digite el nombre del cliente: ")
    return nombre


def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


def calcular_descuento(subtotal, porcentaje):
    descuento = subtotal * porcentaje
    return descuento


def calcular_total_productos(precio1, cantidad1, precio2, cantidad2, porcentaje):
    subtotal1 = calcular_subtotal(precio1, cantidad1)
    subtotal2 = calcular_subtotal(precio2, cantidad2)

    subtotal_general = subtotal1 + subtotal2
    descuento = calcular_descuento(subtotal_general, porcentaje)
    return subtotal1, subtotal2, descuento


def calcular_producto_menor_subtotal(subtotal1, subtotal2):
    if subtotal1 < subtotal2:
        menor = subtotal1
    else:
        menor = subtotal2
    return menor


def calcular_total(precio1, cantidad1, precio2, cantidad2, porcentaje, impuesto):

    subtotal1, subtotal2, descuento = calcular_total_productos(precio1, cantidad1, precio2, cantidad2, porcentaje)

    menor = calcular_producto_menor_subtotal(subtotal1, subtotal2)

    subtotal_general = subtotal1 + subtotal2
    iva = (subtotal_general - descuento) * impuesto
    total = (subtotal_general - descuento) + iva
    return total, subtotal1, subtotal2, descuento, iva, menor


def mostrar_factura(nombre, precio1, cantidad1, precio2, cantidad2, porcentaje, impuesto, total, subtotal1, subtotal2, descuento, iva, menor):
    print("*" * 40)
    print("   FACTURA DE VENTA - TIENDA VALE TODO")
    print("*" * 40)
    print(f"Cliente: {nombre}")
    print("-" * 40)
    print(f"Producto 1: C$ {precio1:.2f} x {cantidad1} = C$ {subtotal1:.2f}")
    print(f"Producto 2: C$ {precio2:.2f} x {cantidad2} = C$ {subtotal2:.2f}")
    print("-" * 40)
    print(f"Subtotal general: C$ {subtotal1 + subtotal2:.2f}")
    print(f"Descuento ({porcentaje * 100:.0f}%): C$ {descuento:.2f}")
    print(f"IVA ({impuesto * 100:.0f}%): C$ {iva:.2f}")
    print(f"Producto con menor importe: C$ {menor:.2f}")
    print("-" * 40)
    print(f"TOTAL A PAGAR: C$ {total:.2f}")
    print("*" * 40)


def main():
    mensaje = "¡Bienvenido a la Tienda Vale Todo!"
    impuesto = 0.15

    nombre = leer_nombre(mensaje)

    print("--- Producto 1 ---")
    precio1 = leer_numero("Digite el precio del artículo: ")
    cantidad1 = int(leer_numero("¿Cuántas unidades va a comprar?: "))

    print("--- Producto 2 ---")
    precio2 = leer_numero("Digite el precio del artículo: ")
    cantidad2 = int(leer_numero("¿Cuántas unidades va a comprar?: "))

    porcentaje = leer_numero("Digite el porcentaje de descuento (ej: 0.10 = 10%): ")

    total, subtotal1, subtotal2, descuento, iva, menor = calcular_total(precio1, cantidad1, precio2, cantidad2, porcentaje, impuesto)

    mostrar_factura(nombre, precio1, cantidad1, precio2, cantidad2, porcentaje, impuesto, total, subtotal1, subtotal2, descuento, iva, menor)


main()