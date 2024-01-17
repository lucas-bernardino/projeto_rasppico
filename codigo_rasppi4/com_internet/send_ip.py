import socket
import requests
import subprocess
import time

time.sleep(35)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def get_api_route():
    command = [ "python3", "aux_email.py"]
    subprocess.run(command)
    with open("rotaapi.txt", "r") as file_:
        return str(file_.readline())

# post_data = session.post(ROTA_API + "/enviar", json=dados_package)

API_ROUTE = get_api_route().rstrip()

print(f"API_ROUTE: {API_ROUTE}")

while True:
    try:
        data_payload = {
            "ip": get_ip()
        }

        print(f'data_payload: {data_payload}')


        api = requests.post(API_ROUTE + "/ip", json=data_payload)
        print(f'response: ', api.status_code)
        if api.status_code == 200: break
    except Exception as e:
        print('got here 2')
        print(e)
    finally:
        time.sleep(5)
