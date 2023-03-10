from datetime import datetime
import time

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
print("Fecha3: ", dt3.strftime("%A, %d of %B, %Y"))

################################
edad = abs(dt3.year - dt1.year)
print(edad)

#################################

# TIME devuelve la cantidad de segundos transcurridos desde el comienzo el tiempo (normalmente 01-Ene-1970 00:00:00)
t1 = time.time()
print(f"Segundos desde 01-01-1970: {t1}")
print("")

# Transformar segundos en una fecha
t2 = time.localtime(t1)
print(f"Tupla: {t2}")
print(f"Propiedad Año: {t2.tm_year}")
print("")

# Convierte una Tupla de tiempo en una representación de fecha y hora local  
print(f"Fecha: {time.asctime(t2)}")
print("")

# Fecha y hora despues de transcurrir 14852 segundos desde 01-01-1970 00:00:00
xt = time.localtime(14852)
print("Después de pasar 14852 desde el 01-Ene-1970 a las 0:00")
print(f"la fecha es: {time.asctime(xt)}")
print("")
