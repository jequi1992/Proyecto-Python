import sqlite3
conexion = sqlite3.connect("C:\sqlite3\BD.db")
con = conexion.cursor()
sql = """
CREATE TABLE IF NOT EXISTS aprendiz(
    idaprendiz INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    edad INTEGER NOT NULL,
    fecnac DATE NOT NULL,
    email VARCHAR(15) NOT NULL)"""
if (con.execute(sql)):
    print("Tabla Aprendiz creada con exito")
else: 
    print("A ocurrido un error.....")
con.close()
conexion.commit()
conexion.close()