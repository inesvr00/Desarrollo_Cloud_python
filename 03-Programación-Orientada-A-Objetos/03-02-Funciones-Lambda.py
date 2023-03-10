numeros = [1, 85, 200, 15, 152, 450, 5, 3601, 63, 77, 8]

def MayorDeCien(lista):
    resultado = []
    
    for item in lista:
        if (item > 100):
            resultado.append(item)
            
    return resultado

print(MayorDeCien(numeros))

#######################################################

def Func1(x):
    if (x > 100):
        return True
    else:
        return False
    
print(list(filter(Func1, numeros)))

########################################################

print(f"Valores mayores de 100: {list(filter(lambda x: x>100, numeros))}")
print(f"Valores pares: {list(filter(lambda x: x % 2 == 0, numeros))}")
print(f"Valores menores de 50 {list(filter(lambda x: x < 50, numeros))}")

########################################################

def Filtrado(formula, datos):
    resultado = []
    for item in datos:
        if (formula(item)) == True: #if (formula(item))
            resultado.append(item)
    return resultado

print(">>>", Filtrado(lambda x: x > 100, numeros))
print(">>>", Filtrado(lambda x: x % 2 != 0, numeros))