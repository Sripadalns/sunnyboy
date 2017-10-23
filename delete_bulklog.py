import requests
import os
from file_clear import clear_file 
max_size = 1024*1024*1024
max_size = 10
try :
    resp = requests.get("http://www.google.com/",timeout = 5)
    
except requests.ConnectionError:
    
    # size in bytes
    size =  os.path.getsize("/home/srinivas/Solar/Prod_v2/AC_Log.csv")
    if size > max_size:
        clear_file("AC_Log.csv")
    
        
    size =  os.path.getsize("/home/srinivas/Solar/Prod_v2/Temp_data.csv")
    if size > max_size:
        clear_file("Temp_data.csv")
    
    
