#####################################################################
# Herncia Multiple de Clases                                        #
#####################################################################

# Definición de la clase A
class A:
    Numero1 = None
    Numero2 = None

    def __init__(self) -> None:
        print("constructo A")

    def Suma(self) -> int:
        return "A>> " + str(self.Numero1 + self.Numero2)
    
    def Resta(self) -> int:
        return "A>> " + str(self.Numero1 - self.Numero2)

# Definición de la clase B
class B:
    Numero1 = None
    Numero2 = None

    def __init__(self, n1, n2) -> None:
        self.Numero1 = n1
        self.Numero2 = n2
        print("constructo B")

    def Suma(self) -> int:
        return "B>> " + str(self.Numero1 + self.Numero2)

    def Multiplica(self) -> int:
        return "B>> " + str(self.Numero1 * self.Numero2)


# Definición de claase Calculadora que hereda de A y B
# Cuando el nombre de las funciones coincide solo puede heredar de una clase
# y prevalece la función de la clase más a la izquierda (espeficada antes)
class Calculadora(A, B): pass

c = Calculadora()
c.Numero1 = 78
c.Numero2 = 15
print(f"Numero1: {c.Numero1}")
print(f"Numero2: {c.Numero2}")
print(f"Suma: {c.Suma()}")
print(f"Resta: {c.Resta()}")
print(f"Multiplica: {c.Multiplica()}")
