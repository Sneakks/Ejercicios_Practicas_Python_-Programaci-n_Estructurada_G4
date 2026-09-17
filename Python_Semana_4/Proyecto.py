import os

def leer_numero(mensaje):

    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo. Intente de nuevo.")
                continue
            return valor
        except ValueError:
            print("Debe digitar un número válido. Intente de nuevo.")


def leer_nombre(mensaje):
    os.system("cls")
    print(mensaje)
    print("*" * 20)
    nombre = input("Digite el nombre del cliente: ")
    return nombre


def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


def calcular_descuento(subtotal, porcentaje):
    descuento = subtotal * porcentaje
    return descuento



def calcular_total_productos(precios, cantidades, porcentaje):

    subtotales = []
    for i in range(len(precios)):
        subtotal = calcular_subtotal(precios[i], cantidades[i])
        subtotales.append(subtotal)

    subtotal_general = sum(subtotales)
    descuento = calcular_descuento(subtotal_general, porcentaje)
    return subtotales, descuento




def calcular_producto_menor_subtotal(subtotales):

    menor = subtotales[0]
    for subtotal in subtotales:
        if subtotal < menor:
            menor = subtotal
    return menor



def calcular_total(precios, cantidades, porcentaje, impuesto):

    subtotales, descuento = calcular_total_productos(precios, cantidades, porcentaje)

    menor = calcular_producto_menor_subtotal(subtotales)

    subtotal_general = sum(subtotales)
    iva = (subtotal_general - descuento) * impuesto
    total = (subtotal_general - descuento) + iva
    return total, subtotales, descuento, iva, menor


def mostrar_factura(nombre, precios, cantidades, porcentaje, impuesto, total, subtotales, descuento, iva, menor):
    print("*" * 40)
    print("   FACTURA DE VENTA - TIENDA VALE TODO")
    print("*" * 40)
    print(f"Cliente: {nombre}")
    print("-" * 40)
    for i in range(len(precios)):
        print(f"Producto {i + 1}: C$ {precios[i]:.2f} x {cantidades[i]} = C$ {subtotales[i]:.2f}")
    print("-" * 40)
    print(f"Subtotal general: C$ {sum(subtotales):.2f}")
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


    num_productos = int(leer_numero("¿Cuántos productos va a comprar?: "))
    precios = []
    cantidades = []
    for i in range(num_productos):
        print(f"--- Producto {i + 1} ---")
        precio = leer_numero("Digite el precio del artículo: ")
        cantidad = int(leer_numero("¿Cuántas unidades va a comprar?: "))
        precios.append(precio)
        cantidades.append(cantidad)

    porcentaje = leer_numero("Digite el porcentaje de descuento (ej: 0.10 = 10%): ")

    total, subtotales, descuento, iva, menor = calcular_total(precios, cantidades, porcentaje, impuesto)

    mostrar_factura(nombre, precios, cantidades, porcentaje, impuesto, total, subtotales, descuento, iva, menor)


main()