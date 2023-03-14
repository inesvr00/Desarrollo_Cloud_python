from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json
# Definir la conexión


# Cuanto productos tenemos ???, buscamos en mongoDB
# Mostramos el múmero de productos y un listo


# Filtrar los productos con UnitsInStock 0, utilizando filter()

# Valor del Stock UnitsInStock x UnitPrice
# con un FOR y otra formula es realizarlo con MAP() SUM()
# con una función AGGREGATE de mongoDB y los operadores $sum y $multiply 


# Con un identificador de pedido
# Mostramos datos -> ShipName, ShipAddress, ShipCity, ShipCountry, OrderDate, ShipDate
# Mostramos el detalle del pedido -> Producto, Cantidad, Precio, Precio Total, Total Pedido

client = MongoClient("mongodb://localhost:27017")
db = client.Northwind
collection = db.Products

num_products = collection.count_documents({})
print("Número de productos: ", num_products)
print("")

print("A continuación se muestran los productos con 0 unidades en stock.")
stock_zero = collection.find(filter = {"UnitsInStock": "0"})
for product in stock_zero:
    print(product['ProductName'])
print("")

# Otra forma de hacerlo
#products = collection.find()
#produ_stock_zero = list(filter(lambda product: int(product["UnitsInStock"]) == 0, collection ))
    
products = collection.find()
stock_value = sum(map(lambda product: int(product["UnitsInStock"]) * float(product["UnitPrice"]), products))
print("Valor del stock:", (round(stock_value, 2)))

products = collection.find()
for product in products:
    stock_value_one = int(product["UnitsInStock"]) * float(product["UnitPrice"])
    print("Producto:", product["ProductName"])
    print("Precio del stock total: ", (round(stock_value_one, 2)))
    
####################################################################################

query = [
    {"$match": {"UnitsInStock" : {"$ne": "0"}}},
    {"$addFields": {
        "Price": {"$toDouble": "$UnitPrice"},
        "Stock": {"$toInt": "$UnitInStock"}
    }},
    {"$group": {
        "_id": "Valor del Stock",
        "Total": {"$sum": {"$multiply": ["$Price", "$Stock"]}},
        "Products": {"$sum": 1}
    }}
]

cursor = db.Products.aggregate(query)
print(cursor.next())


# order_id = 10248
# order = db.Orders.find_one({"OrderID": order_id})
# print("ShipName:", order["ShipName"])
# print("ShipAddress:", order["ShipAddress"])
# print("ShipCity:", order["ShipCity"])
# print("ShipCountry:", order["ShipCountry"])
# print("OrderDate:", order["OrderDate"])
# print("ShipDate:", order["ShippedDate"])

# order_details = db.OrderDetails.find({"OrderID": order_id})
# total_order = 0
# for order_detail in order_details:
#     product = db.Products.find_one({"ProductID": order_detail["ProductID"]})
#     quantity = order_detail["Quantity"]
#     price = order_detail["UnitPrice"]
#     total_price = quantity * price
#     total_order += total_price
#     print("Producto:", product["ProductName"])
#     print("Cantidad:", quantity)
#     print("Precio:", price)
#     print("Precio total:", total_price)

# print("Total pedido:", total_order)


