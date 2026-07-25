cantidad_productos = 4
precio_unitario = 12500
porcentaje_descuento = 10

subtotal = cantidad_productos * precio_unitario
descuento = subtotal * porcentaje_descuento / 100
total_pagar = subtotal - descuento

print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Total a pagar:", total_pagar)
print("La compra supera 40000:", total_pagar > 40000)
