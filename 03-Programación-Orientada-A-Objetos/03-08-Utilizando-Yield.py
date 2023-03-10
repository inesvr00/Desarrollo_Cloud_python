numeros = [8, 14, 65, 7, 14, 99, 745, 1, -35, 1408]

def demo1(lista):
    for i in lista:
        return i * 5

def demo2(lista):
    resultado = []
    for i in lista:
        resultado.append(i * 5)

    return resultado


def demo3(lista):
    for i in lista:
        yield (i * 5)


print("Resultado:", demo3(numeros))
print("Resultado To-List:", list(demo3(numeros)))

generador = demo3(numeros)
print(next(generador))
print(next(generador))
print(next(generador))

generador = demo3(numeros)
for i in generador:
    print(">>", i)

generador2 = ((i * 5) for i in numeros)
print("Next>>>", next(generador2))
print("Next>>>", next(generador2))
for i in generador2:
    print("For>>>", i)

print("Next>->", next(generador2))
print("Next>->", next(generador2))
for i in generador2:
    print("For>->", i)