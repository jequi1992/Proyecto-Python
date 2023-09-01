print("======================================")
print("=**SOLICITA NUMERO WHILE**=")
print("======================================")
contador=1
numero=int(input("Ingrese un número --> "))
while numero>10 or numero<0:
    numero=int(input("Ingrese un numero --> "))
    contador = contador +1
    if(numero==5):
        print("Maximo numero de intentos alcanzados")
        break
print("último Número ingresado: ", numero)
print("Número de intentos: ", contador)
print("-------------------------------------")