import pymssql

# Establecer conexión con la base de datos
connection = pymssql.connect(
        server = "host-sqlserver-eoi.database.windows.net", 
        user = "Administrador", 
        password = "azurePa$$w0rd", 
        database = "Northwind")

# Creamos un cursor para ejecutar comandos en la base de datos
# Retorna Tuplas
cursor = connection.cursor()

# Retorna Diccionarios
cursor = connection.cursor(as_dict = True)

# Ejemplos de comandos SELECT, para recuperar registros de la base de datos
cursor.execute("SELECT * FROM dbo.Customers")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", "Spain")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'Spain' ORDER BY City")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d ORDER BY CITY", "Spain")
# Evitemos el asterisco porque pueden ser muchos campos. Como aquí abajo mejor.
cursor.execute("SELECT CustomerID, CompanyName, Country, City FROM dbo.Customers WHERE Country = 'Spain'")

# Mostrar el contenido del cursor mediante un WHILE
row = cursor.fetchone()
while(row):
    print(f"     ID: {row['CustomerID']}")
    print(f"Empresa: {row['CompanyName']} - {row['Country']}\n")
    row = cursor.fetchone()


# Mostramos el contenido del cursor mediante un FOR
for row in cursor.fetchall():
    # Si trabajamos con diccionarios
    print(f"     ID: {row['CustomerID']}")
    print(f"Empresa: {row['CompanyName']}\n")


# Vamos a insertar datos utilizando el comando INSERT
#result = cursor.execute("INSERT INTO dbo.Customers(CustomerID, CompanyName, ContactName, City, Country) VALUES ('DEMO4', 'Empresa Demo SL', 'Borja Cabeza', 'Madrid', 'Spain')")

command = "INSERT INTO dbo.Customers VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
command = "INSERT INTO dbo.Customers(CustomerID, CompanyName, City, Country) VALUES (%d, %d, %d, %d)"

data = []
data.append(('Inés', 'Empresa Uno Sl', 'Madrid', 'Spain'))
data.append(('Inés', 'Empresa Uno S2', 'Bilbao', 'Spain'))

cursor.executemany(command, data)
connection.commit()
print(f"Número de filas insertadas: {cursor.rowcount}")

# Utilizamos la función commit() para confirmar la trasacción y las operaciones de inserción
# Actualización y borrado
print(connection.commit())

# Utilizamos la función rollback() para cancelar la transacción y anular las operaciones
# de inserción, actualización y borrado
connection.rollback()

exit()

