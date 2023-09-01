import random
print("======================================")
print("=**PROGRAMA SIMULA DADOS - SEIS PUNTOS**=")
print("======================================")
nom=input("Nombre Jugador: ")
lanzamiento=int(input("Ingrese numero de lanzamiento: "))
total=0
for i in range(lanzamiento):
    resdado=random.randrange(1,7)
    print(f"Lanzamiento No. {i+1}: saco {resdado}")
    total=total+resdado
print(f"{nom} el total obtenido es de {total} puntos")
print("==============================================")