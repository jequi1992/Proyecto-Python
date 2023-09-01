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
    if resdado==3:
        cuentaseis=cuentaseis+1
print(f"{nom} En sus {lanzamiento} lanzamiento(s) salieron {cuentaseis} seis")
print("==============================================")