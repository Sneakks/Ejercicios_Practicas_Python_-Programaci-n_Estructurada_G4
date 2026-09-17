def main():
#Inicialización de Variables
    mensaje = "¡Bienvendio a la Tienda Vale Todo!"
    nombre = None
    precio = 0.0
    cantidad = 0
    porcentaje = 0.0
    impuesto = 0.15
    total = subtotal = descuento = iva = 0.0
    #Invocación a leer nombre
    nombre = leer_nombre(mensaje)

    #Invocación a calcular_total
    precio = float(input("Digie el precio del artículo: "))
    cantidad = int(input("¿Cuántas unidades va a comprar?: "))
    Porcentaje = float(input("Digite el porcentaje de descuento: "))
    calcular_total(precio,cantidad,porcentaje,impuesto)

    total,subtotal,descuento,iva = calcular_total(precio,cantidad,porcentaje,impuesto)
    mostrar_factura(nombre,precio,cantidad,porcentaje,impuesto,total,subtotal,descuento,iva)

def leer_nombre(mensaje):
    os.system("cls")
    print(mensaje)
    print("*"* 20)
    nombre = input("Digite el nombre del cliente")
    return nombre

def calcular_total(precio,cantidad,porcentaje,impuesto):
    subtotal = calcular_subtotal(precio,cantidad)
    descuento = calcular_descuento(subtotal,porcentaje)
    iva = (subtotal-descuento) + iva
    total = subtotal
    return total,subtotal,descuento,iva

def calcular_subtotal(precio,cantidad):
    subtotal = precio * cantidad
    return subtotal

def calcular_descuento(subtotal,porcentaje):
    descuento = subtotal * porcentaje
    return descuento

def mostrar_factura(nombre,precio,cantidad,porcentaje,impuesto,total,subtotal,descuento,iva):

    print("*"*40)




    print("*"*40)

