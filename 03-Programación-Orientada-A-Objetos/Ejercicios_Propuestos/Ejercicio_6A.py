# Escribe una función que calcule el precio de una pizza.

# Entrada de datos:

# Ingredientes + Cantidad del ingrediente (almacenar en listas)
# FIN, la cofección de la pizza a finalizado
# Salida de datos:

# Coste de las pizza desglosado

# Ejercicio 6A

def calcular_precio_pizza():
    """
    Esta función calcula el precio de una pizza basado en los ingredientes y su cantidad.
    """
    ingredientes = { "Base": 8.90, "Pepperoni": 0.50, "Pollo": 0.35, "Carne": 0.35, "Pimiento": 0.10, "Cebolla": 0.10}
    precio_total = 0
    
    while True:
        ingrediente = (input("Ingresa un ingrediente (o FIN para terminar): "))
        if ingrediente == "fin":
            break
        if ingrediente not in ingredientes:
            print("El ingrediente ingresado no es válido.")
            continue
        while True:
            try:
                cantidad = int(input("Ingresa la cantidad: "))
                if cantidad <= 0:
                    raise ValueError
                break
            except ValueError:
                print("La cantidad ingresada no es válida. Ingresa un valor numérico positivo.")
        precio_total += ingredientes[ingrediente] * cantidad
    print(f"El precio total de la pizza es: {precio_total:.2f}€")
    
calcular_precio_pizza()