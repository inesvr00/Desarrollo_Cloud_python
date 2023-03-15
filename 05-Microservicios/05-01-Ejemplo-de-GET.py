import requests, pprint

# Endpoint del microservicio
url = "http://api.open-notify.org/iss-now.json"

# Utilizamos la función get() para realizar una llamada GET
# La función get() retorna una respuesta
response = requests.get(url)

# Mostrar el código de estado HTTP
# Mostrar el código de estado HTTP en modo texto utilizando REASON
print(f"Código de Estado: ", response.status_code)
print(f"Estado: ", response.reason)
