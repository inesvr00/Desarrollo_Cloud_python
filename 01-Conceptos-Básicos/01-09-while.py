valor = 0

while (valor < 5):
    valor += 1
    print(f"El valor es {valor}.")
    
print("Fin del while")

######################################

citricos = ["naranja", "limón", "pomelo", "lima", "mandarina"]
index = 0

while index < len(citricos)-1:
    index += 2
    print(f"{citricos[index-1]}")