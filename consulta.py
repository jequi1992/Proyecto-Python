import sqlite3
conexion = sqlite3.connect("C:\sqlite3\BD.db")
con = conexion.cursor()
def consultar():
    con.execute ("SELECT * FROM aprendiz")
    datos =con.fetchall()
    [print(row) for row in datos]
consultar()
conexion.commit()
con.close()
conexion.close()