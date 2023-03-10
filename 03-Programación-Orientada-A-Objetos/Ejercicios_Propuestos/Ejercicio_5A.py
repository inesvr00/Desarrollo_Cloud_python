# Ejercicio 5A
# Escribe un programa que genere un número aleatorio. El usuario escribe números y el programa le responde si acertado y no acertado. Al no acertar debe indicarle si el número es menor o mayar.

# Entrada de datos:

# Número
# Salida de datos:

# Mensajes: has acertado; no has acertado, es menor; no has acertado es mayor

import random

numero_aleatorio = random.randint(1, 20)
print("Adivina el número entre 1 y 20")

while True:
    try:
        numero_ingresado = input("Ingresa un número: ")
        if not numero_ingresado.isdigit():
            raise ValueError
        numero_ingresado = int(numero_ingresado)
        if numero_ingresado < 1 or numero_ingresado > 20:
            raise ValueError
        if numero_ingresado == numero_aleatorio:
            print("¡Has acertado!")
            break
        elif numero_ingresado < numero_aleatorio:
            print("No has acertado, el número es mayor")
        else:
            print("No has acertado, el número es menor")
    except ValueError:
        print("El valor ingresado no es válido. Ingresa un número entre 1 y 20.")