from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

####################################################################################
# CONECTAR CON EL SERVIDOR DE mongoDB
####################################################################################

# Crear el objeto que representa el cliente para trabajar con la base de datos
# Se requiere la cadena de conexión
client = MongoClient("127.0.0.1", 27017)
client = MongoClient("localhost", 27017)
client = MongoClient('mongodb://USUARIO:PASSWORD@localhost:27017/')
client = MongoClient("mongodb://127.0.0.1:27017")
client = MongoClient("mongodb://localhost:27017")



####################################################################################
## MOSTRAR EL ESTADO DEL SERVIDOR DE mongoDB
####################################################################################

# Nos posicionamos en una base de datos utilizando el objeto cliente
db = client.admin

# El comando serverStatus nos retorna el estado del servidor en JSON
status = db.command("serverStatus")
print(status)



####################################################################################
# TRABAJAR CON BASES DE DATOS Y SUS COLECCIONES
####################################################################################

# Mostrar los nombre de las bases de datos
print(client.list_database_names())

# Seleccionar la base de datos con la que vamos a trabajar
db = client.Northwind               # Sintaxis de Objeto
db2 = client["Northwind"]           # Sintaxis de Colección

# Mostrar los nombre de las colecciones de la base de datos seleccionada
print(db.list_collection_names())

# Seleccionar la colección con la que vamos a trabajar
collection = client.Northwind.Customers
collection = client["Northwind"]["Customers"]
collection = db.Customers
collection = db["Customers"]

# Mostrar el número de documentos (registros) en la colección seleccionada
print(f"{collection.estimated_document_count()} documentos en {collection.name}")



####################################################################################
# TRABAJANDO CON DOCUMENTOS DE LAS COLECCIONES
####################################################################################

# Mostrar el primer documento de la colección coincidente con el filtro Country = USA
result = collection.find_one({"Country": "USA"})
pprint(result)
print("")

# Mostrar el primer documento de la colección coincidente con el filtro _id = identificador
id = ObjectId("6409a51eac393e29f975736d")
result = collection.find_one({"_id": id})

# Simplificamos la sentencia de búsqueda anterior
result = collection.find_one({"_id": ObjectId("6409a51eac393e29f975736d")})

pprint(result)
print("")



####################################################################################
# TRABAJANDO CON CURSORES
####################################################################################

# Buscamos en la colección todos los documentos coincidentes con el filtro Country = USA
cursor = collection.find({"Country": "USA"})

# Mostrar el  número de documentos en el cursor (deprecated)
# print(f"Número de documentos en el cursor: {cursor.count()}") 

# Tambíen podemos mostrar el número de documentos sin necesidad de crear el cursor
print("Número de documentos filtrados:", collection.count_documents({"Country": "USA"}))

# ALIVE retorna TRUE si tenemos documentos pendientes de leer en el cursor
print("Datos pendiente de leer:", cursor.alive)

# Utilizamos WHILE para leer los documentos del cursor
# El bloque de WHILE se ejecuta mientras ALIVE retorne TRUE (documentos pendientes de leer en el cursor).
# Con la función .next() nos posicionamos en el siguiente documento del cursor
while (cursor.alive):
    pprint(cursor.next())
    print("")

# ALIVE retorna FALSE cuando no tenemos documentos pendientes de leer en el cursor
print("Datos pendiente de leer:", cursor.alive)
print("")

# También podemos convertir un cursor en una lista y recorrerlo con un FOR
# Debemos tener en cuenta el rendimiento de la conversión, y que el cursor se vacia
cursor = collection.find({"Country": "USA"})

clientes = list(cursor)
print(f"Número de documentos: {len(clientes)}")

for document in clientes:
    print(f"{document['CustomerID']}# {document['CompanyName']}")