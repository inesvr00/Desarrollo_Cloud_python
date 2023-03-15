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


####################################################################################
# EJEMPLOS DE BÚSQUEDAS Y UTILIZACIÓN DE OPERADORES
####################################################################################

"""
===================================================
 Listado de operadores relacionales
===================================================
$eq - equal - igual
$lt - low than - menor que
$lte - low than equal - menor o igual que
$gt - greater than - mayor que
$gte - greater than equal - mayor o igual que
$ne - not equal - distinto
$in - in - dentro de
$nin - not in - no dentro de
"""

cursor = collection.find({"Country": "USA"})
cursor = collection.find({"Country": "USA"}).limit(3)
cursor = collection.find({"Country": "USA"}).skip(5)
cursor = collection.find({"Country": "USA"}).sort("City")       # Ascendente A a W
cursor = collection.find({"Country": "USA"}).sort("City", 1)    # Ascendente A a W
cursor = collection.find({"Country": "USA"}).sort("City", -1)   # Descendente W a A

# Ambas consultas buscan clientes de USA (las dos son iguales)
cursor = collection.find({"Country": "USA"})
cursor = collection.find({"Country": {"$eq" : "USA"}})

# Todos los cliientes que no son de USA
cursor = collection.find({"Country": {"$ne": "USA"}})

# Buscamos clientes de USA y Mexico, ordenados por país y ciudad
cursor = collection.find({"Country": {"$in": ["USA", "Mexico"]}}).sort([("Country", 1), ("City", 1)])

# Buscamos clientes de USA y la ciudad de San Francisco
cursor = collection.find({"Country": "USA", "City": "San Francisco"})

# Buscamos clientes que contienen DE en la clave Customer ID
cursor = collection.find({"CustomerID": {"$regex": "DE"}})

# Consultas utilizando el operador AND
cursor = collection.find({"Country": "USA", "City": "San Francisco"})
cursor = collection.find({"$and": [{"Country": "USA"}, {"City": "San Francisco"}]})

# Consultas utilizando el operador OR
cursor = collection.find({"$or": [{"Country": "USA"}, {"City": "Berlin"}]})
cursor = collection.find({"$or": [{"Country": "USA"}, {"Country": "Germany"}]})


####################################################################################
# SUBCONSULTAS Y AGRUPACIONES
####################################################################################

# Buscamos todos los clientes de Mexico y sus pedidos
cursor = collection.find({"Country": "Mexico"})
while (cursor.alive):
    cliente = cursor.next()
    print(f"{cliente['CustomerID']}# {cliente['CompanyName']}")
    
    cursorPedidos = db.Orders.find({"CustomerID": cliente["CustomerID"]})
    while (cursorPedidos.alive):
        pedido = cursorPedidos.next()
        print(f">>> {pedido['OrderID']} {pedido['OrderDate']}")

    print("")


# Buscamos todos los clientes de Mexico y sus pedidos utilizando AGGREGATE
cursor = db.Customers.aggregate([
   {"$match": {"Country": "Mexico"}},
   {"$sort": {"City": 1}},
   {"$lookup": {
        "from": "Orders",
        "localField": "CustomerID",
        "foreignField": "CustomerID",
        "as": "Orders"
   }}
])

while(cursor.alive):
    customer = cursor.next()
    print(f"{customer['CustomerID']}# {customer['CompanyName']}")
    for order in customer["Orders"]:
        print(f">>> {order['OrderID']} {order['OrderDate']}")
    print("")


# Utilizamos AGGREGATE para calcular el valor del Stock
# Buscamos todos los productos con UnitsInStock distinto de cero
# Convertimos a valor númerico UnitPrice y UnitsInStock
# Sumamos el resultado de multiplicar Price y Stock
query = [
    {"$match": {"UnitsInStock": {"$ne": "0"}}},
    {"$addFields": {
        "Price": {"$toDouble": "$UnitPrice"},
        "Stock": {"$toInt": "$UnitsInStock"}
    }},
    {"$group": {
        "_id": "Valor del Stock",
        "Total": {"$sum": {"$multiply": ["$Price", "$Stock"]}},
        "Products": {"$sum": 1}
    }}
]


cursor = collection.aggregate(query)
print(cursor.next())


####################################################################################
# INSERTAR DOCUMENTOS
####################################################################################

# Insertar un documento en la colección utilizando un diccionario
customer = {
    "CustomerID": "DEMO2",
    "CompanyName": "Uno Comidad y Bebidas, SL",
    "ContactName": "Borja Cabeza",
    "ContactTitle": "Propietario",
    "Address": "Calle Gran Vía, 41",
    "City": "Madrid",
    "Region": "Madrid",
    "PostalCode": "28044",
    "Country": "Spain",
    "Phone": "(91) 200 20 20",
    "Fax": "(91) 200 20 21"
}

idNewDocument = collection.insert_one(customer).inserted_id
print('ID Nuevo Documento: ', idNewDocument)


# Insertamos un documentos en la colección utilizando un objeto de Python
class Customer:
    CustomerID = None
    CompanyName = None
    ContactName = None
    ContactTitle = None
    Address = None
    City = None
    Region = None
    PostalCode = None
    Country = None
    Phone = None
    Fax = None

cliente = Customer()
cliente.CustomerID = "DEMO3"
cliente.CompanyName = "Un Dos Tresm, SL"
cliente.ContactName = "Borja Cabeza"
cliente.ContactTitle = "Generente"
cliente.Address = "Calle Gran Vía, 16"
cliente.Region = "Madrid"
cliente.City = "Madrid"
cliente.Country = "Spain"
cliente.PostalCode = "28024"
cliente.Phone = "(91) 200 20 20"
cliente.Fax = "(91) 300 30 30"

# La propiedad __dict__ de cualquier objeto nos devuelve un diccionario que representa
# todos los valores contenidos en las variables
pprint(cliente.__dict__)

idNewDocument = client.Northwind.customers.insert_many(cliente.__dict__).inserted_id
print('ID Nuevo Documento: ', idNewDocument)


####################################################################################
# ACTUALIZAR DOCUMENTOS
####################################################################################

# Actuliazamos documentos en una colección
# Consulta, determina los documentos que se tienen que modificar
query = {'CustomerID': 'DEMO2'}

# Determina las claves y valores que son modificados en los documento encontrados por la consulta
newValues = {
    "$set": {
        "CompanyName": "Restaurantes Dos, SL",
        "Address": "Calle Serrano, 81",
        "Phone": "(91) 400 80 80"
    }
}

# Actualizar el primer documento coincidente con el filtro de búsqueda
result = collection.update_one(query, newValues)

# Actualizar todos los documentos coincidentes con el filtro de búsqueda
result = collection.update_many(query, newValues)

print(result.matched_count, ' elementos encontrados.')
print(result.modified_count, ' elementos modificados.')
pprint(result)
pprint(collection.find_one(query))


####################################################################################
# ELIMINAR DOCUMENTOS
####################################################################################

# Eliminar el primer documento coincidente con el filtro de búsqueda
result = collection.delete_one({'CustomerID': 'DEMO2'})

# Eliminar todos los documentos coincidentes con el filtro de búsqueda
result = collection.delete_many({'CustomerID': 'DEMO2'})

print(result.deleted_count, 'elementos eliminados.')
pprint(result)