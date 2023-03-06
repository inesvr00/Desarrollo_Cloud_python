# Requerimientos funcionales:
#
#   - Calcular la velocidad en km/h
#   - La información la tenemos en metros y minutos
#   - Clasificar en alta, baja o moderada
#   - Alta por encima de 75 km/h; Baja por debajo de
#     30 km/h; el resto moderada.
####################################################
try:
    vel_ms = int(input("Introduce la velocidad en m/s: "))
except:
    print("Error. Introduce un valor numérico.")
    exit()

vel_kmh = vel_ms / 1000 * 3600

if (vel_kmh > 75):
    print(f"La velocidad introducida es de {vel_kmh} km/h, por lo que,"
          f"al ser mayor que 75 km/h, se clasifica como velocidad alta.")
elif (vel_kmh < 30):
    print(f"La velocidad introducida es de {vel_kmh} km/h, por lo que,"
          f"al ser menor que 30 km/h, se clasifica como velocidad baja")
else:
    print(f"La velocidad introducida es de {vel_kmh} km/h, por lo que,"
          f"al encontrarse entre (30 - 70) km/h, se clasifica como"
          f"una velocidad moderada")