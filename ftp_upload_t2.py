import ftplib
import os
import re
from file_clear import clear_file
import time

def upload(file):
    timestr = time.strftime("%Y%m%d_%H%M%S")
    
    try:
        ftp = ftplib.FTP("148.66.137.40")
        ftp.login("pasr", "kmcWL@r4&hBGXl")
        ext = os.path.splitext(file)[1]
        sfname = os.path.splitext(file)[0]
        dfname= sfname+"_"+timestr+ext
        path = os.path.join("/home/pasr","/TagData")
        if ext in (".txt", ".htm", ".html"):
                ftp.cwd(path)
                rx = ftp.storlines("STOR " + dfname, open(file))
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






