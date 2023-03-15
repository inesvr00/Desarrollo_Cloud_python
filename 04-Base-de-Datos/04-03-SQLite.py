import sqlite3, json

# Establecemos conexión con la base de datos, indicamos la ruta del fichero,
# Si el fichero no existe se crea
connection = sqlite3.connect("demo.db")

# Creamos un cursor que nos permite ejecutar comandos en la base de datos
cursor = connection.cursor()

# command = "CREATE TABLE Profesores (id integer, salario real, nombre text, apellidos text, curso text, foto blob)"
# cursor.execute(command)

# Creamos una base de datos en memoria RAM
# connection = sqlite3.connect(":memory:")

# Consultamos la existencia de una tabla en la base de datos
# Si la tabla no existe, se crea 
command = "SELECT count() FROM sqlite_master WHERE type = 'table' AND name = 'Alumnos'"
cursor.execute(command)
numTables = cursor.fetchone()[0]
print(f"Número de tablas Alumnos: {numTables}")

if (numTables == 0):
    command = "CREATE TABLE Alumnos (id, nombre, apellidos, curso, notas)"
    cursor.execute(command)
    print(f"Número de tablas creadas: {cursor.rowcount}")
    

   
# Consultar datos con SELECT
command = "SELECT * FROM Alumnos"
cursor.execute(command)

row = cursor.fetchone()
while(row):
    print(row)
    row = cursor.fetchone()
    
print("")

cursor.execute(command)

exit()

 # Insertamos datos utilizando INSERT
command = "INSERT INTO Alumnos (id, nombre) VALUES ('001', 'Inés')"   
cursor.execute(command)
connection.commit()
command = "INSERT INTO Alumnos VALUES ('002', 'María', 'Peñasco', '4A', Null)"   
cursor.execute(command)
connection.commit()

# Insertamos varios registros
lista = [
    ('003', 'Julian', 'Wayne', '2A', None),
    ('004', 'Paz', 'Padilla', '2C', None),
    ('005', 'Jorge', 'Esteban', '1A', json.dumps([7.5, 6, 7, 4])),
]
command = "INSERT INTO Alumnos VALUES (?, ?, ?, ?, ?)"
cursor.executemany(command, lista)
connection.commit()
print("Número de registros insertados: ", cursor.rowcount)  

# Actualizamos un registro utilizando UPDATE
command = "UPDATE Alumnos SET apellidos = 'Victoria' WHERE id = '001'"
cursor.execute(command)
connection.commit()
print(f"Número de registros modificados: {cursor.rowcount}")

# Eliminamos a María

command = "DELETE FROM Alumnos WHERE nombre = 'María'"
cursor.execute(command)
connection.commit()
print(f"Número de registros eliminados: {cursor.rowcount}")
    