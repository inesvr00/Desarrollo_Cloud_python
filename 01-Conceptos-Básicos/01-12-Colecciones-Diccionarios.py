vacio = {}
frutas = {"NA":"naranja", "LI":"pimiento", "PO":"pomelo", "LM":"limón", "MA":"mandarina"}

# Mostras el diccionario 
print(frutas)

# Mostrar un valor utilizando la clave
# Si la clave no existe se produce una Exception
print(frutas["NA"])

# Mostrar un valor utilizando la función GET
# Si la clave no existe la función GET retorna el valor None
print(frutas.get("NA"))
print(frutas.get("NI"))

# Mostrar el número de valores del diccionario
print(len(frutas))

# Modificar el valor de un elemento
frutas["LI"] = "limón"
print(frutas["LI"])

# Añadir un nuevo valor al diccionario
frutas["ME"] = "melón"

# Eliminar un valor utilizando la clave
frutas.pop("PO")
del frutas["LM"]

# Recorremos y mostramos todos los valores del diccionario utilizando FOR
for key in frutas:
    print(f"Clave: {key} - Valor: {frutas[key]}")
print(frutas)