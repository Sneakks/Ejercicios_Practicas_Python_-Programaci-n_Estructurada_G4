def precioProducto():
    try:
        prod = float(input("Ingrese el precio del producto: "))
    except ValueError:
        print("Ingrese únicamente números enteros o con decimáles")
    else:
        print("Precio del producto registrado exitósamente; ",prod)