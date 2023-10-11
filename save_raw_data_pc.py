import subprocess

def saveRawData():
  pico_file = "dados.txt"
  local_file = "dados_pico.txt"
  com_port = "COM6"  # Substitua pelo seu valor

  with open("dados_pico.txt", "w") as create_file:
    pass

  command = f"ampy --port {com_port} get {pico_file} {local_file}"

  try:
    subprocess.run(command, shell=True, check=True)
  except subprocess.CalledProcessError as e:
    print("An error has occurred", e)

