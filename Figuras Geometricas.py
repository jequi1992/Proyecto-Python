print("===============================================")
print("= *** AREA Y PERIMETRO FIGURAS GEOMETRICAS*** =")
print("===============================================")
print("1.Rectangulo\n 2.Cuadrado \n3.Rombo\n4.Triangulo\n 5.Salir")
print("-------------------------------------")
op = int(input("elijauna figura"))
usu=(input("Nombre usuario: "))
usuario=usu.upper()
if op==1:
    print("* OPERACIONES PARA RETANGULO***")
    print("-------------------------------------")
    print("1.Hallar Area\n2 Hallar perimetro\n3. salir")
    op1=int(input("elija  operacion"))
    print("--------------------------------------")
    if op1==1:
        print("* AREA DEL RETANGULO***")
        base=int(input("valor de base : " ))
        altura=int(input("valor altura :"))
        area=base*altura
        print(f"{usuario} el area del retangulo es de {area}")
        print("---------------------------------------------")
    elif op1 == 2:
        print("* perimetro del retangulo***")
        base=int(input("valor de base :"))
        altura=int(input("valor altura:"))
        perimetro = base*2 + altura*2
        print(f"{usuario} el perimetro del retangulo es el {perimetro}")
        print("--------------------------------------------")
    elif op1 == 3:
        print(f" {usuario} eligio salir del programa")
    else:
        print(f"{usuario} -->ERROR ELEGIO UNA OPCION NO VALIDA ")

elif op==3:
    print("*** OPERACIONES PARA ROMBO***")
    print("-------------------------------------------")
    print("1. Hallar Area\n2. Hallar Perimetro\n3. Salir")
    op1=int(input("Elija Operacion :"))
    print("-------------------------------------------")
        
    if op1==1:
        print("*** AREA DEL ROMBO ***")
        diagmayor=int(input("Valor Diagonal Mayor :"))
        diagmenor=int(input("Valor Diagonal Menor:"))
        area=(diagmayor*diagmenor)/2
        print(f"{usuario} el area del Rombo es de {area}")
        print("-----------------------------------------")
    elif op1==2:
        print("*** PERIMETRO DEL ROMBO ***")
        lado=int(input("Valor Lado :"))
        perimetro =4*lado
        print(f"{usuario} el area del Rombo es de {perimetro}")
        print("-----------------------------------------")
    elif op1==3:
        print(f"{usuario} Eligio Salir del Programa\n")
    else:
        print(f"{usuario} --> ERROR ELIGIO UNA OPCION NO VALIDA")
elif op==4:
    print("*** OPERACIONES PARA TRIANGULO ***")
    print("-----------------------------------------")
    print("1. Hallar Area\n2. Hallar Perimetro\n3. Salir")
    op1=int(input("Elija Operacion :"))
    print("-------------------------------------------")
    if op1==1:
        print("*** AREA DEL TRIANGULO ***")
        base=int(input("Valor Base :"))
        altura=int(input("Valor Altura:"))
        area=(base*altura)/2
        print(f"{usuario} el area del Triangulo es de {area}")
        print("-----------------------------------------")
    elif op1==2:
        print("*** PERIMETRO DEL TRIANGULO ***")
        lado=int(input("Valor Lado :"))
        perimetro =lado*3
        print(f"{usuario} el perimetro del Triangulo es de {perimetro}")
        print("-----------------------------------------")
    elif op1==3:
        print(f"{ usuario} Eligio Salir del Programa\n")
    else:
        print(f"{usuario} --> ERROR ELIGIO UNA OPCION NO VALIDA")
else:
    print(f"{usuario} Debe Elegir una Opcion entre 1 y 5")
            
        
        
        
            
    
        
    