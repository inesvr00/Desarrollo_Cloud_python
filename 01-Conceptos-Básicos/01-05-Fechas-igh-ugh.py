from datetime import datetime

# Año, mes, día
dt1 = datetime.now().date()
print(f'Fecha 1: {dt1}')
print("Día: ", dt1.day) 

# Completo
dt2 = datetime.now()
print(f'Fecha 2: {dt2}')
print("Hora: ", dt2.hour) 

#############################

strFecha = input("Escribe tu fecha de nacimiento: ")
dt3 = datetime.strptime(strFecha, "%d-%m-%Y").date()

print(f'Fecha de nacimiento: {dt3}')

################################
edad = abs(dt3.year - dt1.year)
print(edad)