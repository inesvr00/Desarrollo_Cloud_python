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
print("")

if (response.status_code == 200):
    print("Cabeceras: ", response.headers)
    print("")
    print("Content-Type: ", response.headers["Content-Type"])
    print("")
    print(f"Content-Length: {response.headers['Content-Length']} bytes")
    print("")
    print("Contenido: ", response.content)
    print("")
    
    if (response.headers["Content-Type"] == "application/json"):
        data = response.json()
        print(f"Mensaje: {data['message']}")
        print(f"Marca de tiempo: {data['timestamp']}")
        print(f"Fecha: {data['timestamp']}")
        print(f"Longitud: {data['iss_position']['longitude']}")
        print(f"Latitud: {data['iss_position']['latitude']}")
    else:
        print("No se pueden procesar los datos")
        
else:
    print(f"Error: ", response.reason)
    
##############################################################################

url = "https://postman-echo.com/post"

myHeaders = {"content-type": "application/json", "api-key": "Anastasia Beverly Hills"}

# Enviar datos en la URL
url = "https://dominio.com/api/customers/100/orders"

# Enviar datos como cabecera
url = "https: // dominio.com/api/customers"
myHeaders = {
    "content-type": "application/json",
    "api-key": "Anastasia Beverly Hills",
    "id": 100,
    "process": "orders"
}

# Enviar datos en el curpo del mensaje

url = "https: // dominio.com/api/customers"

mydata = {
    "id": 100,
    "process": "orders"
}

url = "https://postman-echo.com/post"

myHeaders = {"content-type": "application/json", "api-key": "jKHduyad5askfj8d$m8s"}
myParams = {"id": 100, "process": "orders"}
mydata = {"id": 100,"process": "orders"}

#response = requests.post(url, params=myParams, headers=myHeaders, data=mydata)
response = requests.request(
    "POST", url, params=myParams, headers=myHeaders, data=mydata
)

print(f"Código de Estado: ", response.status_code)
print(f"Estado: ", response.reason)
print("Cabeceras: ", response.headers)
print("Contenido: ", response.text)