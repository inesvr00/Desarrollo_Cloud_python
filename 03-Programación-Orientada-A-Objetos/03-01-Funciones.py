def Saludo(nombre):
    print(f'Hola me llamo {nombre}')
    
Saludo('Inés')

saludo = lambda nombre : print(f'Hola me llamo {nombre}')
saludo("Inés")


def Multiplicar(num):
    return lambda a: a * num

print(Multiplicar(25))

def operacion(num1=None, num2=None, operacion_elegida=None):
    if None in (num1, num2, operacion_elegida):
        raise ValueError("Se requieren tres argumentos: num1, num2 y operacion_elegida")
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

