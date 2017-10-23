def set_time(datetime):
    print " Entered"
    import os
    import time
    sudopass = '12345'
    cmd  = datetime
    print cmd
    os.system('echo %s | sudo -S %s' %(sudopass,cmd))
    time.sleep(60)
    os._exit(0)
