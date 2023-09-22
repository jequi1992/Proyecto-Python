import sqlite3
print ("___________________________________ ")
print ("*** REGISTRAR DE APRENDICES SENA ***")
print ("___________________________________ ")
nombre = input("Ingrese Nombre Aprendiz:  ")
edad = int(input("Ingrese edad Aprendiz: "))
fecnac = input ("Ingrese Fecha Nacimiento: ")
email = input ("Ingrese email Aprendiz: ")
conexion = sqlite3.connect("C:\sqlite3\BD.db")
con = conexion.cursor()
atributos = (nombre, edad, fecnac, email)
sql = """
INSERT INTO aprendiz (nombre,edad,fecnac,email)
VALUES(?,?,?,?)
"""
if (con.execute(sql,atributos)):
    print("===========================")
    print ("Aprendiz Registrado en la BS")
else:
    print("Error en Registro de Aprendiz")

conexion.commit()
con.close()
conexion.close()