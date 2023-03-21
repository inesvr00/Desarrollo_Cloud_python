import requests, json

loginHeader = {
    "X-ClientID" : "e5a7e34e-27ce-49c6-a79a-cf578a09b9fe",
    "passKey" : "5E06F9AA4E91E99C18165C8FAE43B1A30010D9B68AE91A63BF5ED2CEB1FC2035288DE6EABEEB0C5987F3705570B235D77DCBCE1F9132B6BB00183201F1C60B91"
}

urlLogin = f"https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/"

try:
    response = requests.get(urlLogin, headers = loginHeader)
    print()
    if(response.status_code == 200):
        data = response.json()
        token = data['data'][0]['accessToken']
        
except:
    print(f"Error : {response.reason}")
    
urlBus = "https://openapi.emtmadrid.es/v1/transport/busemtmad/stops/125/detail/"

tokenHeader = {
    "accessToken" : token
}

print(token)

myBody = {
    "cultureInfo":"ES",
    "Text_StopRequired_YN":"Y",
    "Text_EstimationRequired_YN":"Y",
    "Text_IncidencesRequired_YN":"N",
    "DateTime_Referenced_Incidencies_YYYYMMDD":"20230321"
}

Body_json = json.dumps(myBody)

try: 
    response = requests.get(urlBus, headers = tokenHeader, data=Body_json)
    print(response.status_code, response.reason)
    if(response.status_code == 200):
        data = response.json()
        print(data)
        for i in data['data'][0]['Arrive']:
            print(f"La guagua {i['bus']} llega a la parada {i['stop']}")
except:
    print(f"Error : busStop")
            