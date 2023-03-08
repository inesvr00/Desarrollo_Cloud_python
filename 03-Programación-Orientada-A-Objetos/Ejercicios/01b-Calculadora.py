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
        
print(operacion(num2 = 9, operacion_elegida='dividir'))
print(operacion(num2 = 9, num1 = 3 operacion_elegida='dividir'))