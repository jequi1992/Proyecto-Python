import sqlite3
print ("*** REGISTRAR DE APRENDICES SENA ***")
print ("___________________________ ")
conexion = sqlite3.connect("C:\sqlite3\BD.db")
cur = conexion.cursor()
sql = """
INSERT INTO Aprendiz VALUES(30, "HOMERO", 45, "10/08/1975","homerosi@sena.edu.co")
"""
cur.execute(sql)
sql ="""
INSERT INTO Aprendiz VALUES(15, "MARCH", 40, "2/09/1970","marchis@sena.edu.co")
"""
cur.execute(sql)
sql ="""
INSERT INTO Aprendiz VALUES(3, "BARTOLOMEO", 18, "2/07/2008","barsis@sena.edu.co")
"""
cur.execute(sql)
print ("APRENDICES AGRAGADOS EXITOSAMENTE")
conexion.commit()
cur.close()
conexion.close()
