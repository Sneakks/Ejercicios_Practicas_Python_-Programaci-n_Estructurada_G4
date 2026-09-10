import os


def leer_numero(mensaje):
    """Subproblema: Leer un número seguro.
    Entrada: mensaje (texto a mostrar).
    Salida: número válido (float) que el usuario digitó."""
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
    """Subproblema: Calcular subtotal.
    Entrada: precio, cantidad. Salida: subtotal."""
    subtotal = precio * cantidad
    return subtotal


def calcular_descuento(subtotal, porcentaje):
    """Subproblema: Calcular descuento.
    Entrada: subtotal, porcentaje. Salida: descuento."""
    descuento = subtotal * porcentaje
    return descuento


def calcular_total(subtotal, descuento, impuesto):
    """Subproblema: Calcular total.
    Entrada: subtotal, descuento, impuesto. Salida: total (e iva, como dato extra)."""
    iva = (subtotal - descuento) * impuesto
    total = (subtotal - descuento) + iva
    return total, iva


def mostrar_factura(nombre, precio, cantidad, porcentaje, impuesto, total, subtotal, descuento, iva):
    """Subproblema: Presentar factura. Entrada: resultados. Salida: texto en pantalla."""
    print("*" * 40)
    print("   FACTURA DE VENTA - TIENDA VALE TODO")
    print("*" * 40)
    print(f"Cliente: {nombre}")
    print(f"Precio unitario: C$ {precio:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: C$ {subtotal:.2f}")
    print(f"Descuento ({porcentaje * 100:.0f}%): C$ {descuento:.2f}")
    print(f"IVA ({impuesto * 100:.0f}%): C$ {iva:.2f}")
    print("-" * 40)
    print(f"TOTAL A PAGAR: C$ {total:.2f}")
    print("*" * 40)


def main():
    mensaje = "¡Bienvenido a la Tienda Vale Todo!"
    impuesto = 0.15

    nombre = leer_nombre(mensaje)

    precio = leer_numero("Digite el precio del artículo: ")
    cantidad = int(leer_numero("¿Cuántas unidades va a comprar?: "))
    porcentaje = leer_numero("Digite el porcentaje de descuento (ej: 0.10 = 10%): ")

    subtotal = calcular_subtotal(precio, cantidad)
    descuento = calcular_descuento(subtotal, porcentaje)
    total, iva = calcular_total(subtotal, descuento, impuesto)

    mostrar_factura(nombre, precio, cantidad, porcentaje, impuesto, total, subtotal, descuento, iva)


if __name__ == "__main__":
    main()