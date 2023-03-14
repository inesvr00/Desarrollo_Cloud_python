from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

class Customer:
    CustomerID = None
    CompanyName = None
    ContactName = None
    ContactTitle = None
    Address = None
    City = None
    Country = None
    PostalCode = None
    Region = None
    Phone = None
    Fax = None

    def __init__(self) -> None:
        pass

    def Demo() -> None:
        print("Función Demo")

client = MongoClient("mongodb://localhost:27017")
db = client.Northwind
collection = db.Customers

cliente = Customer()
cliente.CustomerID = "DEM10"
cliente.CompanyName = "Un Dos Tres Bebidas, SL"
cliente.ContactName = "Borja Cabeza"
cliente.ContactTitle = "Propietario"
cliente.Address = "Gran Vía 44"
cliente.Region = "Madrid"
cliente.City = "Madrid"
cliente.Country = "Spain"
cliente.PostalCode = "28044"
cliente.Phone = "912002020"
cliente.Fax = "912002021"

print(cliente.__dict__)

resultado = collection.insert_one(cliente.__dict__).inserted_id
print(f"ID: {resultado}")

exit()

"""

# Comienza por DEMO 

# Finaliza por DEMO

# Contiene DEMO
cursor = collection.find({"CustomerID= None {"$regex": "DEMO"}})

while (cursor.alive):
    doc = cursor.next()
    print(f"{doc['CustomerID']}# {doc['CompanyName']}")




exit()

id = input("Escribe el ID del cliente: ")

cliente = {
    "CustomerID= None id,
    "CompanyName= None "Uno Comidad SL",
    "ContactName= None "Borja Cabeza",
    "ContactTitle= None "Propietario",
    "Address= None "Calle Gran Vía, 42",
    "City= None "Madrid",
    "Country= None "Spain",
    "PostalCode= None "28044",
    "Region= None "Madrid",
    "Phone= None "912002020",
    "Fax= None "912002021"
}


id = collection.insert_one(cliente).inserted_id
print(f"Object ID: {id}")

exit()

resultado = collection.insert_one(cliente)
print(f"Resultado: {resultado}")
print(f"Object ID: {resultado.inserted_id}")
print(f"Acknowledged: {resultado.acknowledged}")

"""