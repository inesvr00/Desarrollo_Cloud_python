from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

client = MongoClient("mongodb://localhost:27017")
db = client.Northwind
collection = db.Customers

query = {"Country": "USA"}
newValues = {
    "$set": {
        "Country": "Estados Unidos",
    }
}

print(collection.count_documents(query), "Clientes USA")
result = collection.update_many(query, newValues)
print(result.matched_count, "documentos encontrados")
print(result.modified_count, "documentos modificados")
print(result)
print(collection.count_documents(query), "Clientes USA")
print(collection.count_documents({"Country": "Estados Unidos"}), "Clientes Estados Unidos")

exit()

query = {"CustomerID": "DEM10"}
documento = collection.find_one(query)
pprint(documento)

newValues = {
    "$set": {
        "Address": "Calle Serrano, 81",
        "PostalCode": "28016",
        "Phone": "914502525"
    }
}

result = collection.update_one(query, newValues)
print(result.matched_count, "documentos encontrados")
print(result.modified_count, "documentos modificados")
print(result)
pprint(collection.find_one(query))