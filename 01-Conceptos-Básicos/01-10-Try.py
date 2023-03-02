import sys

num1 = 0
num2 = 100

try:
    num3 = num2 / num1
    print(f"Resultado: {num3}")
    f = open("myfile.txt")
except ZeroDivisionError as err:
    print("Upppss!! Se ha producido un error")
    print(err)
    print(type(err))
except FileNotFoundError as err:
    print("El fichero no existe")
    print(err)
    print(type.err)
except:
    print("Se ha producido un error")
finally:
    print("Bloque FINALLY")
    
print("Fin")