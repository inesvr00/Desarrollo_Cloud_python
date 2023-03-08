# def nombre():
#     print("Función nombre")
    
# def saludo(texto):
#     print("Función saludo")
#     print(f"Contenido de texto: {texto}")
#     texto = "Nuevo valor"
#     print(f'Contenido de texto {texto}')
    
# def demo(): pass

# class Persona: pass

# numeros = [10, 7, 5, 7, 6]
# def suma_mi_lista(lista):
#     result = sum(lista)
#     print(result)

# suma_mi_lista(numeros)

# def suma(num1, num2):
#     num3 = num1 + num2
#     while (num3 > 100):
#         if (num3 > 100):
#             return num3
#         else:
#             print(num3)
#             num3 += 10


# resultado = suma(10, 40)
# print(resultado)

# nombre()
# saludo("Mari Paz")
# print(type(nombre))
# print(type(demo))
# print(type(Persona))

# def resta(a, b):
#     c = a + b
#     return c

# print(resta(10, 30))
# print(resta(b = 10, a = 20))

# def demo(lista):
#     for item in lista:
#         print(item)
        
# def demo2(*lista):
#     for item in lista:
#         print(item)
        
# demo([5, "Hola", [1, 2, 3, 4, 5]])

# demo2(5, "Hola", [1, 2, 3, 4, 5])

# Posición 0: un número

# Posición 1: un número

# Posición 2: un texto con la operación a realizar -> sum, res, div, mul

def operacion(num1, num2, operacion_elegida):
    operaciones = {
        'suma': lambda: num1 + num2,
        'resta': lambda: num1 - num2,
        'dividir': lambda: num1 / num2,
        'multiplicar': lambda: num1 * num2,
    }
    
    operacion_elegida = operacion_elegida.lower()
    
    if operacion_elegida not in operaciones:
        raise ValueError("La operación elegida no existe")
        
    return operaciones[operacion_elegida]()
        
print(operacion(2, 3, 'dividir'))