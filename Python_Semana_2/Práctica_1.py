import os
os.system("cls")

compra = float(input("Monto en C$: "))

if compra >= 1500:
    descuento = 0.10 
elif compra >= 800:
    descuento = 0.05
else:
    descuento = 0

total = compra - compra *descuento
print("Total en C$: ", total)