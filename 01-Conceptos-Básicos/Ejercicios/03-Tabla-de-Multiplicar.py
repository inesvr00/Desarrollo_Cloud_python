# Requerimientos funcionales:
#
#   - Mostrar la tabla de multiplicar del número
#     indicado por el usuario
#   - Resolver con un FOR y con un WHILE
#
#################################################

numero = int(input("Introduce el número para generar su tabla de multiplicar: "))

# Ejemplo utilizando FOR
try:
    for veces in range(0, 11, 1):
        resultado = numero * veces
        print(f"{numero} x {veces} = {resultado}")
except:
    print("Introduzca un número entero.")
    exit()

print("")

# Ejemplo utilizando WHILE
contador = 0
while contador < 11:
    result = numero * contador
    contador += 1
    print(f"{numero} x {contador-1} = {result}")