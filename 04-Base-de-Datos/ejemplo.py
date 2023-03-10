from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

client = MongoClient("mongodb://localhost:27017")
db = client.Northwind
collection = db.Customers

# Ambas buscan clientes de Estados Unidos
cursor = collection.find({"Country": "USA"})
cursor = collection.find({"Country": {"$eq" : "USA"}})

# Todos los clientes que no son de Estados Unidos
cursor = collection.find({"Country": {"$ne" : "USA"}})

# Buscamos clientes de Estados Unidos y México
cursor = collection.find({"Country": {"$in" : ["USA", "Mexico"]}}).sort("Country")

# Buscamos clientes de USA y la ciudad de San Francisco
cursor = collection.find({"Country": "USA", "City": "San Francisco"})

# Ordenar por dos campos o más
# Una consulta con dos campos y operador OR
cursor = collection.find({"$and" : [{"Country": "USA", "City": "San Francisco"}]})

cursor = collection.find({"$or": [{"Country": "USA"}, {"Country": "Germany"}]})


cursor = collection.find({"Country": "USA"}).limit(3)
cursor = collection.find({"Country": "USA"}).skip(5)
cursor = collection.find({"Country": "USA"}).sort("City")  # Ascendente de A a W
cursor = collection.find({"Country": "USA"}).sort("City", 1) # Ascendente de A a W
cursor = collection.find({"Country": "USA"}).sort("City", -1) # Ascendente de W a A


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


while (cursor.alive):
    d = cursor.next()
    print(f"{d['CompanyName']} {d['Country']} {d['City']}")
    print("")
    
exit()
    