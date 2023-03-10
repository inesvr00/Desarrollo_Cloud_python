# Ejercicio 9A
# Escribe un programa que muestre el nombre del día de la semana del cumpleaños del usuario desde su nacimiento hasta hoy.

# Entrada de datos:

# Fecha de nacimiento
# Salida de datos:

# Nombre del día de la semana de cada año
import datetime

def mostrar_dia_semana_cumpleaños():
    fecha_nacimiento = input("Ingresa tu fecha de nacimiento en formato dd/mm/aaaa: ")
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    fecha_actual = datetime.datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    for i in range(edad):
        fecha_cumple = datetime.datetime(fecha_nacimiento.year + i, fecha_nacimiento.month, fecha_nacimiento.day)
        dia_semana_cumple = fecha_cumple.strftime("%A")
        print(f"Cumpleaños {i + 1}: {dia_semana_cumple}")
