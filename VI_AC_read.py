def onemin_task():
    global samplesize
    global vrms
    global irms
    global voltageAC
    global currentAC
    global insPower

    
    rms = ( voltageAC / samplesize)
    vrms = np.sqrt(rms)
    irms = ( currentAC / samplesize)
    irms = np.sqrt(irms)
    ap_power = vrms*irms
    active_power = (insPower/samplesize)
    reactive_power = np.sqrt(np.square(ap_power) -np.square(active_power))
    
    data_log_fn("AC_Log.csv",vrms,"Vrms")
    data_log_fn("AC_Log.csv",irms,"Irms")
    data_log_fn("AC_Log.csv",ap_power,"Apparent Power")
    data_log_fn("AC_Log.csv",active_power,"Active Power")
    data_log_fn("AC_Log.csv",reactive_power,"Reactive Power")
   
    
    print vrms,irms,ap_power,active_power,reactive_power
    samplesize = 0
    voltageAC  = 0
    currentAC  = 0
    insPower    = 0
    threading.Timer(60,onemin_task).start()

def qhour_task():
   upload("AC_Log.csv")
   threading.Timer(900,qhour_task).start()

global voltageAC
global currentAC
global samplesize
global insPower

samplesize = 0
voltageAC = 0
currentAC = 0
insPower  = 0

global vrms
global irms
from datetime import datetime
import time
import os
from ADC_SPI import *
from millis import current_milli_time
import numpy as np
import threading
from data_log_fn import data_log_fn
from ftp_upload import upload

# SPI channel 2 for AC Voltage
AC_V_chanl = 2

# SPI channel 3 for AC Current
AC_I_chanl = 3

# Pull up resistance for Sensor
R1 = 1000

#Reference ADC voltage. Need to read from GSM M66
Vref = 5

min_timer = threading.Timer(60,onemin_task)     
min_timer.start()
qhour_timer = threading.Timer(900,qhour_task)     
qhour_timer.start()
base_time = current_milli_time()
spi = MCP3208(0)
while (1):
        current_time = current_milli_time()
        if ( current_time - base_time > 4 ):
           base_time = current_time
           #ADC_SPI init
           
           AC_V_count =  spi.read(AC_V_chanl)
           AC_I_count =  spi.read(AC_I_chanl)
           AC_V = round ( (( AC_V_count* Vref)/float(4095)) ,5)
           AC_V = (AC_V - 2.5) *500

           AC_I= round ( (( AC_I_count* Vref)/float(4095)) ,5)
           AC_I = (AC_I - 2.5) *40
           
           power = AC_V*AC_I
           insPower  = insPower+power
                  
           voltageAC = voltageAC + np.square(AC_V)
           currentAC = currentAC + np.square(AC_I)
           samplesize = samplesize + 1
          



    





    
