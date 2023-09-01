print("=======================")
print("Programa para calcular el valor a pagar de un Producto")
print("=======================")
producto = input("Ingrese el nombre del producto:   ")
vlrunitario = float(input("Ingrese el precio del producto:  "))
cant = float(input("Ingrese la cantidad a comprar:   "))
vlrproducto = cant*vlrunitario
dineropaga = float(input("Valor que paga es:  "))
dev = dineropaga - vlrproducto 
print("El valor del producto es:   ",vlrproducto)
print("El dinero entregado fue de:  ",dineropaga) 
print("El valor a devolver al cliente es de:   ",dev)
print("**Gracias por su Compra**")