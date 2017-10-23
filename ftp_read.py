import ftplib
import os
import re
from file_clear import clear_file 

def upload(file):
    try:
        ftp = ftplib.FTP("148.66.137.40")
        ftp.login("pasr", "kmcWL@r4&hBGXl")
        ext = os.path.splitext(file)[1]
        path = os.path.join("/home/pasr","/TagData")
      #  print path
        if ext in (".txt", ".htm", ".html"):
                ftp.cwd(path)
                rx = ftp.storlines("STOR " + file, open(file))
                res =re.search('File successfully transferred', rx)
                
                if res is not None:
                    clear_file(file)
                   
        else:
                ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
        ftp.quit()
    except:
        print " Network is unreachable"
        
    #file.close()
    

upload("AC_Log.txt")






