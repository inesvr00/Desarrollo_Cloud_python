# Buscar los clientes de Mexico
# Mostrarnos su información del cliente CustomerID + CompanyName
# Mostramos sus pedidos

from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

client = MongoClient("mongodb://host-mongodb-eoi.northeurope.cloudapp.azure.com:27017")
db = client.Northwind
customers = db.Customers
orders = db.Orders


mexican_customers = customers.find({"Country": "Mexico"})

counter = 1

while(mexican_customers.alive):
    print(f'Cliente {counter}')
    customer = mexican_customers.next()
    print(f"{customer['ContactName']} - {customer['CompanyName']}")
    
    customer_pedidos = db.Orders.find({"CustomerID": customer["CustomerID"]})
    while (customer_pedidos.alive):
        pedido = customer_pedidos.next()
        print(f">>> {pedido['OrderID']} {pedido['OrderDate']}")
    
    print("")
    
# Los datos de ANATR y todos sus pedidos
cursor = customers.aggregate([
    { "$match": {"CustomerID": "ANATR"}},
    {"$sort": {"City": 1}},  # Esto no tiene sentido pero lo ponemos como ejemplo
    {"$lookup": {
        "from": "Orders",
        "localField": "CustomerID",
        "foreignField": "CustomerID",
        "as": "Orders" # Esto es para cambiarle el nombre, podríamos poner "pedids" por ejemplo
    }}
])

# Como solo tenemos un cliente no haría falta poner while
while (cursor.alive):
    customer = cursor.next()
    print(f"{customer['CustomerID']} # {customer['CompanyName']}")
    for order in customer['Orders']:
        print(f">>> {order['OrderID']} {pedido['OrderDate']}")