print("***programa de prestamo**")
nombre=input("ingrese nombre del cliente: ")
num_cedula=input("ingrese numero de documento: ")
valorprestar= float(input("valor a  prestar: "))
valorintereses=0.15
mesesprestamo= int(input("ingrese meses de prestamo:"))
interes= valorprestar*valorintereses 
cuotamensual= valorprestar/mesesprestamo
valorcuotatotal=interes+cuotamensual
valortotalprestamo=valorcuotatotal*mesesprestamo
print("nombre del cliente: ",nombre)
print("numero de documento: ",num_cedula)
print("valor  prestar: ",valorprestar) 
print("valor cuota",cuotamensual)
print("valor a pagar interes incluidos: ",valorcuotatotal)
print("valor total pretamo es:",valortotalprestamo)