import requests, json

# Pongo mi hearder con lo que me pide la api
loginHeader = {
    "X-ClientID" : "e5a7e34e-27ce-49c6-a79a-cf578a09b9fe",
    "passKey" : "5E06F9AA4E91E99C18165C8FAE43B1A30010D9B68AE91A63BF5ED2CEB1FC2035288DE6EABEEB0C5987F3705570B235D77DCBCE1F9132B6BB00183201F1C60B91"
}

# Comienzo el proceso para obtener mi token a través del login
urlLogin = f"https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/"

try:
    response = requests.get(urlLogin, headers = loginHeader)
    print()
    if(response.status_code == 200):
        data = response.json()
        token = data['data'][0]['accessToken']
# En caso de que no funcione me lo dice
except:
    print(f"Error : {response.reason}")

# Comienzo el proceso para obtener la availability de los aparcamients donde 
# me piden el token para poder acceder
urlAparc = "https://openapi.emtmadrid.es/v1/citymad/places/parkings/availability"

tokenHeader = {
    "accessToken" : token
}

try: 
    # Para generar response le doy el url de los aparcamientos y el token
    # que es necesario para acceder
    response = requests.get(urlAparc, headers = tokenHeader)
    print(response.status_code, response.reason)
    # Si el status es 200 (correcto) procedo
    if(response.status_code == 200):
        # Convierto mi response a objeto
        json_data = response.json()
        # Utilizo filter para que con el 'freeParking' dentro de 'data' dentro
        # de mi json_data me sume únicamente los valores no None (no null)
        filter_data = filter(lambda item: item["freeParking"] is not None, json_data["data"])
        # Sumo todo lo que se encuentre el filter_data
        total = sum(item["freeParking"] for item in filter_data)
        print(f"Los parkings totales que hay son: {total}")
except:
    print(f"Error")