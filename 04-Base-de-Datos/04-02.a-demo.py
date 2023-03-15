import pymssql

# Establecer conexión con la base de datos
connection = pymssql.connect(
        server = "host-sqlserver-eoi.database.windows.net", 
        user = "Administrador", 
        password = "azurePa$$w0rd", 
        database = "Northwind")

cursor = connection.cursor(as_dict = True)

id = input("Identificador: ")

# cursor.execute("SELECT * FROM dbo.Customers WHERE CustomerID = 'DEMO1'")
# for row in cursor.fetchall():
#     print(f" ID: {row['CustomerID']}")
#     print(f"Empresa: {row['CompanyName']}\n")
               
# cursor.execute("UPDATE dbo.Customers SET CompanyName = 'Comidas y Bebidas 2, SL' WHERE CustomerID = 'DEMO1'")


# connection.commit()
# print(f"Número de filas modificadas:", cursor.rowcount)

cursor.execute("DELETE * FROM dbo.Customers WHERE CustomerID = 'DEMO1'")
cursor.execute("DELETE * FROM dbo.Customers WHERE CustomerID = %d", id)
connection.commit()
print(f"Número de filas eliminadas: ", cursor.rowcount)

connection.close()

exit()