import ftplib
import os
import re
from file_clear import clear_file
import time

def upload(file):
    timestr = time.strftime("%Y%m%d_%H%M%S")
    print timestr
    
    try:
        ftp = ftplib.FTP("148.66.137.40")
        ftp.login("pasr", "kmcWL@r4&hBGXl")
        ext = os.path.splitext(file)[1]
        print ext
        sfname = os.path.splitext(file)[0]
        dfname= sfname+"_"+timestr+ext
        
        path = os.path.join("/home/pasr","/TagData")
        ftp.cwd(path)
        if ext in (".txt", ".htm", ".html",):
                rx = ftp.storlines("STOR " + dfname, open(file))
        if ext ==".csv":
               dfname= sfname+"_"+timestr+".csv"
               rx = ftp.storbinary("STOR " + dfname, open(file, "rb"), 1024)       
        else:
                rx = ftp.storbinary("STOR " + dfname, open(file, "rb"), 1024)
        res =re.search('File successfully transferred', rx)
        if res is not None:
                    clear_file(file)
        ftp.quit()
        print dfname
    except:
        print " Network is unreachable"








