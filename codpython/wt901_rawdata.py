from witmotion import IMU
from time import sleep
import pandas as pd

string = []
array_pandas = []

def callback(msg, string=string):
    string.append(str(msg))
    
    if len(string) == 4:
        with open("dadosloop550.txt", "a") as f:
            f.writelines(str(string))
            f.write("\n")

        print(string)
        
        array_pandas.append(string)
        
        string.clear()
    
    if len(array_pandas) == 4*20:
        df = pd.DataFrame(array_pandas)
        df.to_excel("dados2.xlsx")
        return
    


imu = IMU("COM5") 
imu.subscribe(callback)
