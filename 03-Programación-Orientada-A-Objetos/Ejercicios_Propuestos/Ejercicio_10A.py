# Ejercicio 10A
# Escribe una función que pinte por pantalla un triangulo, cuadrado o circulo. Utiliza como máximo 10 sentencias print.

# Entrada de datos:

# tipo de figura
# Salida de datos:

# figura impresa
def imprimir_figura(tipo_figura):
    if tipo_figura == "triangulo":
        print("    *    ")
        print("   ***   ")
        print("  *****  ")
        print(" ******* ")
    elif tipo_figura == "cuadrado":
        print("*********")
        print("*       *")
        print("*       *")
        print("*       *")
        print("*********")
    elif tipo_figura == "circulo":
        print("   ******  ")
        print("  *      * ")
        print(" *        *")
        print("*          *")
        print(" *        *")
        print("  *      * ")
        print("   *****  ")
    else:
        print("Tipo de figura no válido. Las opciones son 'triangulo', 'cuadrado' o 'circulo'.")