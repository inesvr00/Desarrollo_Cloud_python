import requests

url = f"https://api.apilayer.com/exchangerates_data/convert?to=USD&from=EUR&amount=80"
myHeaders = {
    "apikey": "WqVzJ6pWHbPkkil5ya8tzBYyBM2fKj1z"
}

c_to = input("Moneda a llegada (USD): ")
c_from = input("Moneda de partida (EUR): ")
c_amount = input("Cantidad a convertir: ")

if(c_to == ""):
    c_to = "USD"
    
myParams = {
    "to": c_to,
    "from": c_from,
    "amount": c_amount
}

try:
    response = requests.get(url, headers=myHeaders, params=myParams)
    
    if(response.status_code == 200):
        data = response.json()
        print(f"\nConversión:\n {data['query']['amount']} {data['query']['from']} >>>> {data['result']} {data['query']['to']}")
    else:
        print(f"Razón: {response.reason}")
except:
    print("Error")

exit()

url = f"htpps://api.apilayer.com/exchangerates_data/symbols"
headers = {"apikey": "WqVzJ6pWHbPkkil5ya8tzBYyBM2fKj1z"}

try:
    response = requests.get(url)
    if (response.status_code == 200):
        data = response.json()
        print(data)
    else:
        print(f"Error: ", response.response.reason)
except Exception as err:
    print(f"Error: {err}")
exit()

url_base = "http://api.zippopotam.us/es/"
codigo_postal = input("Introduce un código postal: ")

url = url_base + codigo_postal

try:
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        print("Headers:")
        print(respuesta.headers)
        print("")
        print("Datos:")
        data = respuesta.json()
        print(data)
        print("")
        print(respuesta.json()["places"][0]["place name"])
        print("")
    for i in data["places"]:
        print(i['place name'])
        print(i['state'])
    else:
        print(f"Error", respuesta.reason)
except Exception as err:
    print(f"Error: {err}")