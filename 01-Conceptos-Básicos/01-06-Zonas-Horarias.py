from datetime import datetime, timedelta, timezone
from pytz import timezone
import pytz

# Mostrar las zonas horarias disponibles
# print(pytz.all_timezones)

# Mostrar fecha actual
dt = datetime.now()
print(dt)

dt_tokyo = datetime.now(pytz.timezone("Asia/Tokyo"))
print(f'La hora en Tokyo es: {dt_tokyo}')

dt_madrid = datetime.now(pytz.timezone("Europe/Madrid"))
print(f'La hora en Madrid es: {dt_madrid}')

dt_alaska = datetime.now(pytz.timezone("US/Alaska"))
print(f'La hora en Alaska es: {dt_alaska}')