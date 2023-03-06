# Utilizamos corchetes [] para crear listas
frutas = ["naranja", "pera", "mandarina", "lima", "melón", "uva"]
vacia = []

# Mostrar el contenido de una lista
print(frutas)

# Mostrar el valor contenido en una posición (2 = mandarina)
print(frutas[2])

# Mostrar número de elementos que contiene la lista
print(len(frutas))

# Mostrar el número de veces que se repite un valor
print(frutas.count("pera"))

# Modificar el valor de una posición
frutas[3] = "fresa"
print(frutas[3])

# Añadir un nuevo valor utilizando la función APPEND
frutas.append("manzana")
frutas.append("tomate")
print(frutas)

# Añadir un nuevo valor utilizando la función INSERT
frutas.insert(1, "arándano")
print(frutas)

# Añadir si el valor no existe
if ("plátano" not in frutas):
    frutas.append("plátano")
    
# Añadir varios valores procedentes de una lista con EXTEND(values)
nuevasFrutas = ["maracuyá", "kiwi", "guayaba"]
frutas.extend(nuevasFrutas)

# Eliminar un valor en base a la posición utilizando POP(index)
frutas.pop(5)

# Eliminar un valor en base a su contenido utilizando REMOVE(value)
frutas.remove("tomate")

# Eliminar un valor si existe
if ("sandía" in frutas):
    frutas.remove("sandía")
print(frutas)

# Invertir el orden de los valores utilizando REVERSE
frutas.reverse()

# Ordenar los valores utilizando SORT
frutas.sort()
frutas.sort(reverse = True)

# Recorremos la lista y mostramos los valores
for fruta in frutas:
    print(fruta)
    
# Copiar todos los valores de la lista
vacia = frutas.copy()
print(vacia)

# Eliminar todos los valores de la lista
frutas.clear()
print(frutas)