import subprocess

def saveNumberOfFiles():
  number_files_pico = "number.txt"
  number_files_pc = "number_pc.txt"
  com_port = "COM6" 

  with open("number_pc.txt", "w") as create_file:
    pass

  command = f"ampy --port {com_port} get {number_files_pico} {number_files_pc}"

  try:
    subprocess.run(command, shell=True, check=True)
  except subprocess.CalledProcessError as e:
    print("An error has occurred", e)
    
def saveRawData():
    
    saveNumberOfFiles()
    
    number = open("number_pc.txt", "r")
    
    n_times = int(number.read()[-1]) + 1
    
    for n in range( n_times ):
        file_pico = f"dados{str(n)}.txt"
        file_pc = f"dados_pc{str(n)}.txt"
        com_port = "COM6"
        
        with open(file_pc, "w") as f:
            pass
        
        command = f"ampy --port {com_port} get {file_pico} {file_pc}"

        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print("An error has occurred", e)
            
if __name__ == "__main__":
    saveRawData()
