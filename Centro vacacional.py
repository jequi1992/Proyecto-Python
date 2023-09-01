print ("BIENVENIDOS AL CENTRO RECREACIONAL MORIDERO")
nombre = input("Ingrese el nombre del empleado:   ")
valorsalariom = float(input("Ingrese el valor del salario minimo:   "))
valorsueldo = float(input("Ingrese el valor del sueldo: "))
ingreso = int(input("Ingrese el numero de personas que ingresan: "))
print("Nombre del empleado:   ",nombre)
if valorsueldo == 0 and ingreso == 0 :
    print("NO PUEDEN HABER VALORES EN CERO")
if valorsueldo<=valorsalariom :
   valorpasadia = (0.02*valorsueldo)*ingreso
   print("Su Categoria es la: A")
elif valorsueldo>valorsalariom and valorsueldo<=2500000 :
    valorpasadia = (0.04*valorsueldo)*ingreso
    print("Su Categoria es la: B")
elif valorsueldo>2500000 and valorsueldo<=3500000 :
    valorpasadia = (0.06*valorsueldo)*ingreso
    print("Su Categoria es la: C")
else: 
    valorsueldo >3500000
    valorpasadia = (0.08*valorsueldo)*ingreso
    print("Su Categoria es la: D") 
print("El valor  a pagar es de:    ",valorpasadia)