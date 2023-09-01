import random
print("======================================")
print("=**PROGRAMA SIMULA DADOS - SEIS PUNTOS**=")
print("======================================")
nom=input("Nombre Jugador: ")
lanzamiento=int(input("Ingrese numero de lanzamiento: "))
cuentaseis=0
for i in range(lanzamiento):
    resdado=random.randrange(1,7)
    print(f"Lanzamiento No. {i}:{resdado}")
    if resdado==6:
        cuentaseis=cuentaseis+1
print(f"{nom} En sus tres lanzamiento salieron {cuentaseis} seis")
print("==============================================")