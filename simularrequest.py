import requests

dados_package = {
  "id": "0",
  "acel_x": "-0.0765625",
  "acel_y": "0.1435546875",
  "acel_z": "9.771289062500001",
  "vel_x": "0",
  "vel_y": "0",
  "vel_z": "0",
  "roll": "-1.4556884765625",
  "pitch": "0.2471923828125",
  "yaw": "143.096923828125",
  "mag_x": "9.84375",
  "mag_y": "-13.16162109375",
  "mag_z": "16.9244384765625",
  "temp": "30.07",
  "esterc": '121.488',
  "rot": '999',
  "veloc": "0",
  "long": "0",
  "press_ar": "0.9970984455958549",
  "altitude": "24.5",
  "lat": "0",
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

