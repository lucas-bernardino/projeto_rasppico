from os import system
from time import sleep
from subprocess import check_output
import json

system('ngrok start --all --log=stdout >/dev/null &')

sleep(1)

data_to_write = {
    "backend": "",
    "frontend": "",
    "flask": ""
}

#TODO: Handle possible errors.
response = check_output(['curl', 'localhost:4040/api/tunnels']).decode("utf-8")
response_json = json.loads(response)
for elm in response_json["tunnels"]:
    match elm["name"]:
        case "backend":
            data_to_write["backend"] = elm["public_url"]
        case "frontend":
            data_to_write["frontend"] = elm["public_url"]
        case "flask":
            data_to_write["flask"] = elm["public_url"]


print("\n\nUsing the following URLS:")
__import__('pprint').pprint(data_to_write)

def change_dotenv_flask():
    with open("backend/.env", "r+") as file:
        lines = file.readlines()
        if lines[-1] == "\n":
            lines[-2] = f'BACKEND_URL={data_to_write["backend"]}'
        else:
            lines[-1] = f'BACKEND_URL={data_to_write["backend"]}'
        file.seek(0)
        for line in lines:
            file.write(line)

def change_dotenv_react():
    with open("frontend/vite-project/.env", "r+") as file:
        lines = file.readlines()
        print(lines)
        lines[0] = f'VITE_BACKEND_URL={data_to_write["backend"]}\n'
        if lines[-1] == "\n":
            lines[-2] = f'VITE_FLASK_URL={data_to_write["flask"]}'
        else:
            lines[-1] = f'VITE_FLASK_URL={data_to_write["flask"]}'
        file.seek(0)
        for line in lines:
            file.write(line)


def save_urls_in_file():
    with open("urls-ngrok.txt", "a") as file:
        json.dump(data_to_write, file)

change_dotenv_react()
change_dotenv_flask()
