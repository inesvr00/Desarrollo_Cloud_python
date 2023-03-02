

# Cambiar los valores de a y b. Intento 1.
a = 5
b = 10

print("Intento 1. Forma Incorrecta.")
print(a)
print(b)
print("")

# Cambiar los valores de a y b. Intento 2.
a = 5
b= 10

temp = a
a = b
b = temp

print("Intento 2. Funciona, pero un poco raro in my opinion.")
print(a)
print(b)
print("")

# Cambiar los valores de a y b. Intento 3.
a = 5
b = 10

a,b = b,a

print("Intento 3. Funciona, forma preferida de Python")
print(a)
print(b)