# Requerimientos funcionales:
#
#   - Calcular la edad
#   - Mostrar si es mayor de edad
#   - Años que le faltan para ser mayor de edad
#
#################################################
from datetime import datetime

cumple = input("Por favor introduce tu fecha de nacimiento: ")
try:
    cumple = datetime.strptime(cumple, '%d-%m-%Y').date()
except:
    print("El formato de la fecha no es válido.")
    
actual = datetime.now().date()

living_days = actual - cumple
años = living_days.days // 365

print(f"Tienes {años} años.")

if años >= 18:
    print("Eres mayor de edad.")
else:
    faltan = 18 - años
    print(f"Te faltan {faltan} años para ser mayor de edad.")
