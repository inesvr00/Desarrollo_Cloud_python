# Ejercicio 1A
# Escribe una función para calcular el consumo medio de combustible de un vehículo.

# Entrada de datos:

# Kilometros recorridos
# Listros de combustible consumidos
# Salida de datos:

# litros consumidos por kilimetro

def Consumo(km = None, litros = None):
    if None in (km, litros):
        raise ValueError("Se requieren dos argumentos: km y litros")
    
    if not isinstance(km, (int, float)) or not isinstance(litros, (int, float)):
        raise TypeError("Ambos argumentos deben ser números")
    
    try:
        consumo = litros / km
    except ZeroDivisionError:
        raise ValueError("El valor de km no puede ser cero")
    
    print(f"El consumo de este coche es de {consumo} l/km")
    
Consumo('hola', 5)