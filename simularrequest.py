import requests

dados = {'acel_z': '9.81'}
res = requests.post('http://localhost:3000/enviar', json=dados)
print(res.text)

dados = requests.get('http://localhost:3000/receber')
print(dados.json())

