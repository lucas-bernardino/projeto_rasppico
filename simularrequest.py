import requests

dados_package = {
    "vel_x": "30.52",
    "vel_y": "40.12",
    "vel_z": "50.23",
    "temp": "26.65",
    "acel_x": "60.23",
    "acel_y": "65.54",
    "acel_z": "69.44",
    "roll": "123.84",
    "pitch": "25.65",
    "yaw": "312.81",
    "mag_x": "548.85",
    "mag_y": "654.47",
    "mag_z": "94.63",
}
res = requests.post('http://localhost:3000/enviar', json=dados_package)
print(res.text)

dados = requests.get('http://localhost:3000/receber')
print(dados.json())

