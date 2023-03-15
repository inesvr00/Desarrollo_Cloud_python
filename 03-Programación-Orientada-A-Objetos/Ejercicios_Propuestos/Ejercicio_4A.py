# Ejercicio 4A
# Escribe una función que cuente las vocales de una frase.

# Entrada de datos:

# Una frase
# Salida de datos:

# Número de vocales desglosado

def contar_vocales(frase):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in frase:
        if letra.lower() in vocales:
            vocales[letra.lower()] += 1
    for vocal, cantidad in vocales.items():
        print(f"{vocal}: {cantidad}")


frase = "Hola me llamo Inés"
contar_vocales(frase)
