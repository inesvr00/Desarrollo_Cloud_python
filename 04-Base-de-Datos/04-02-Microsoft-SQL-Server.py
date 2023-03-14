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