def data_log_modem_fn (filenum,value,sensor_info):
    import serial
    import time
    from datetime import datetime
    
    ser =serial.Serial()
    ser.port = "/dev/ttyAMA0"
    ser.baudrate = 9600
    ser.bytesize = serial.EIGHTBITS #number of bits per bytes
    ser.parity = serial.PARITY_NONE #set parity check: no parity
    ser.stopbits = serial.STOPBITS_ONE #number of stop bits
    ser.timeout = 1            #non-block read
    ser.xonxoff = False     #disable software flow control
    ser.rtscts = False     #disable hardware (RTS/CTS) flow control
    ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
    ser.writeTimeout = 2     #timeout for write

    ser.open()

    print ser.isOpen()
    ser.write('AT'+'\n')
    print ser.read(50)
    time.sleep(0.5)

    ser.write('AT+CPIN?'+'\n')
    print ser.readall()
    time.sleep(0.5)

    ser.write('AT+CREG?'+'\n')
    print ser.readall()
    time.sleep(0.5)

    ser.write('AT+COPS?'+'\n')
    print ser.readall()
    time.sleep(0.5)

    ser.write('AT+CGATT?'+'\n')
    print ser.readall()
    time.sleep(0.5)

    ser.write('AT+QIFGCNT=0'+'\n')
    print ser.readall()
    time.sleep(0.5)

    ser.write('AT+QIREGAPP'+'\n')
    print ser.readall()
    time.sleep(0.5)

    ser.write('AT+QIACT'+'\n')
    print ser.readall()
    time.sleep(0.5)

    ser.write('AT+QILOCIP'+'\n')
    print ser.readall()
    time.sleep(0.5)

    ser.write('AT+QFTPUSER="pasr"'+'\n')
    print ser.readall()
    time.sleep(0.5)

    ser.write('AT+QFTPPASS="kmcWL@r4&hBGXl"'+'\n')
    print ser.readall()
    time.sleep(0.5)

    ser.write('AT+QFTPCFG=2,0'+'\n')
    print ser.readall()
    time.sleep(0.5)

    ser.write('AT+QFTPOPEN="148.66.137.40",21'+'\n')
    print ser.readall()
    time.sleep(60)

    if ( filenum == 1):
        ser.write('AT+QFTPPUT="Temp_panel_Log.txt",34,100'+'\n')
        time.sleep(1)
        print ser.readall()
    elif (filenum == 2):
        ser.write('AT+QFTPPUT="Temp_box_Log.txt",34,100'+'\n')
        time.sleep(1)
        print ser.readall()
    else:
        ser.write('AT+QFTPPUT="Temp.txt",46,100'+'\n')
        time.sleep(1)
        print ser.readall()


    ser.write(str(value))
    ser.write("\t")
    ser.write(str(datetime.now()))
    ser.write("\n")

    print ser.readall()



    time.sleep(30)


    ser.write('AT+QFTPCLOSE'+'\n')
    print ser.readall()
    time.sleep(0.5)


    ser.write('AT+QIDEACT'+'\n')
    print ser.readall()
    time.sleep(1)




    ser.close()

