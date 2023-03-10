class A:
    num1 = 0
    num2 = 0
    
    def __init__(self) -> None:
        pass
    
    def Suma(self) -> int:
        return self.num1 + self.num2
    
    def Resta(self) -> int:
        return self.num1 - self.num2
    
class B:
    numero1 = None
    numero2 = None
    
    def __init__(self, n1, n2) -> None:
        self.numero1 = n1
        self.numero2 = n2
    
    def Suma(self) -> int:
        return self.numero1 + self.numero2
    
    def Resta(self) -> int:
        return self.numero1 - self.numero2
    
class Calculadora(B, A): pass

c = Calculadora(36, 18)

print(f"Número1: {c.num1} - {c.numero1}")
print(f"Número1: {c.num2} - {c.numero2}")
print(f"Suma: {c.Suma()}")