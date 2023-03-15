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


#######################################################################
# Requerimientos funcionales:
#
#   -> Mostrar información ordenada y detallada de un pedido
#   -> Mostrar: ShipName, ShipAddress, ShipCity, ShipCountry, OrderDate, ShipDate
#   -> Mostrar: Producto, Cantidad, Precio, Precio Total linea
#   -> Mostrar: Total del Pedido
#######################################################################

from pymongo import MongoClient

# Cliente
client = MongoClient('mongodb://localhost:27017/')

# Base de Datos
db = client.Northwind

# Colecciones
orders = db.Orders
details = db.Order_Details
products = db.Products


idPedido = input("Identificador del Pedido: ")

pedido = orders.find_one({'OrderID': idPedido})
if (pedido != None):
    print(f"===============================================================")
    print(f" DATOS DEL PEDIDO {idPedido}")
    print(f"===============================================================")
    print(f" Entregar : {pedido['ShipName']}")
    print(f"            {pedido['ShipAddress']}")
    print(f"            {pedido['ShipCity']} ({pedido['ShipCountry']})")
    print("")
    print(f"    Fecha : {pedido['OrderDate']}")
    print(f"  Enviado : {pedido['ShippedDate']}")
    # Buscamos el detalle del pedido
    detalle = details.find({'OrderID':  idPedido})
    print(f"===============================================================")
    print(f"  {'Producto':<31} {'Cant. '} {'Precio':>10} {'Total':>10}")
    print(f"===============================================================")

    totalPedido = 0

    # Recorremos con While el curso del detalle del pedido
    while (detalle.alive):
        linea = detalle.next()
        # Buscasmos y mostramos la descripción del producto, utilizando ProductID
        producto = products.find_one({'ProductID': linea['ProductID']})
        # Mostramos cada linea de pedido
        # Descripción  -  cantidad  - precio  -  precio * cantidad
        totalLinea = int(linea['Quantity']) * float(linea['UnitPrice'])
        totalPedido += totalLinea

        totalFormat = "{:0.2f}".format(totalLinea)

        print(
            f"  {producto['ProductName']:<31} {linea['Quantity']:>6} {linea['UnitPrice']:>10} {totalFormat:>10}")

    # Mostar el importe total del pedido
    print(f"===============================================================")
    totalPedidoFormat = "{:0.2f}".format(totalPedido)
    print(f"  {'TOTAL':>49} {totalPedidoFormat:>10}")
else:
    print(f"El pedido {idPedido} no existe.")


