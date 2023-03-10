# Escribe una función que indique los aciertos de una combinación de loteria primitiva. Una vez introducidos los datos se genera la combinación ganadora utilizando siguiente código:

# import random
# n = random.randint(1, 49)

# La combinación ganadora se compone de 6 números no iguales.

# Entrada de datos:

# Introduce 6 número distintos entre 1 y 49
# Salida de datos:

# Número de aciertos

import random

def comprobar_aciertos():
    combinacion_ganadora = random.sample(range(1, 50), 6)
    
    print("Introduce 6 números distintos entre 1 y 49:")
    combinacion_usuario = []
    
    while len(combinacion_usuario) < 6:
        try:
            numero = int(input(f"Ingresa el número {len(combinacion_usuario) + 1}: "))
            if numero < 1 or numero > 49:
                raise ValueError
            if numero in combinacion_usuario:
                print("El número ingresado ya fue elegido.")
                continue
            combinacion_usuario.append(numero)
        except ValueError:
            print("El valor ingresado no es válido. Ingresa un número entero entre 1 y 49.")
    num_aciertos = len(set(combinacion_usuario).intersection(combinacion_ganadora))
    print(f"Número de aciertos: {num_aciertos}")
    
comprobar_aciertos()