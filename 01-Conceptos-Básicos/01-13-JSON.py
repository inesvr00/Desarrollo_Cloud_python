import json

animales = ["elefante", "perro", "gato", "caballo", "culebra", "hormiga", "perezoso"]
animales_JSON = json.dumps(animales)

print(animales)
print(type(animales))
print("")

print(animales_JSON)
print(type(animales_JSON))
print("")

print(animales[3])
# Al printear la posición lo trata como un str (lo que es)
print(animales_JSON[5])
print("")

animales2 = json.loads(animales_JSON)
print(animales2)