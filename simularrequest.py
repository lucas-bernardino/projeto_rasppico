import requests

dados_package = {
    "id": "1",
    "acel_x": "111.23",
    "acel_y": "95.54",
    "acel_z": "50.44",
    "vel_x": "30.52",
    "vel_y": "540.12",
    "vel_z": "904.23",
    "roll": "43.84",
    "pitch": "35.65",
    "yaw": "56.54",
    "mag_x": "31.85",
    "mag_y": "54.47",
    "mag_z": "96.63",
    "temp": "123",
    "esterc": "541",
    "rot": "432",
    "veloc": "543",
    "long": "21",
    "lat": "54",
    "press_ar": "1000",
    "altitude": "23443",
}

# Enviar para Mongo
# NAO ESQUECER DE ACRESCENTAR O ID NO DICIONARIO
res = requests.post('http://localhost:3000/enviar', json=dados_package)
print(res.text)

# # Receber todos do Mongo
# dados_all = requests.get('http://localhost:3000/receber')
# print(dados_all.json())

# # Receber por ID do Mongo
# dados_id = requests.get('http://localhost:3000/receber/652adb76d3636ea4e95fa54c')
# print(dados_id.json());

