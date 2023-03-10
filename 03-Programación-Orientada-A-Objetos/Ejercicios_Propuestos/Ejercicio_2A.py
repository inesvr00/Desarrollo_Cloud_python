# Ejercicio 2A
# Escribir funciones para tranformar grados Celsius en Fahrenheit y viciversa.

# Formulas: Celsius = (5 ÷ 9) x (Fahrenheit - 32) Fahrenheit = (Celsius x (9 ÷ 5)) + 32

# Entrada de datos:

# Grados Celsius/Fahrenheit
# Salida de datos:

# Grados transformados

def celsius_a_fahrenheit (celc):
    fahr = (celc * 9 / 5) + 32
    return fahr

def fahrenheit_a_celsius(fahrenheit):
    """
    Convierte una temperatura en grados Fahrenheit a grados Celsius.
    La fórmula utilizada es: (F - 32) * 5/9, donde F es la temperatura en Fahrenheit.
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# Ejemplo de uso:
celsius = 25
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit")

fahrenheit = 80
celsius = fahrenheit_a_celsius(fahrenheit)
print(f"{fahrenheit} grados Fahrenheit son {celsius:.2f} grados Celsius")