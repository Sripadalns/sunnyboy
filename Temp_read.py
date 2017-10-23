from GSM_Modem_working import data_log_modem_fn
from ftp_upload import upload
from Temp_lookup import get_TempSensorVal
from data_log_fn import data_log_fn
from ADC_SPI import *
import time
 
# Pull up resistance for Temp Sensor
R1 = 1000

#Reference ADC voltage. Need to read from GSM M66
Vref = 5

#ADC_SPI
spi = MCP3208(0)

# SPI channel 0 for panel Temprature
panel_temp_chanl = 0


# SPI channel 1 for Box Temprature
box_temp_chanl = 1


# Read panel Temperature
PV_temp_count=  spi.read(panel_temp_chanl)
PV_temp_V = round ( (( PV_temp_count* Vref)/float(4095)) ,3)
PV_temp_R = ( R1 * PV_temp_V ) / (Vref - PV_temp_V)

#pass R and sensor sample (1=free,2=Paid) to read the deg C
Panel_PV_temp = round(get_TempSensorVal(PV_temp_R, 1) )
data_log_fn("Temp_data.csv",Panel_PV_temp,"Panel temp")
#data_log_modem_fn(1,Panel_PV_temp,"Panel temp")

# Read Box Temperature
PV_temp_count=  spi.read(box_temp_chanl)
PV_temp_V = round ( (( PV_temp_count* Vref)/float(4095)) ,3)
PV_temp_R = ( R1 * PV_temp_V ) / (Vref - PV_temp_V)

#pass R and sensor sample (1=free,2=Paid) to read the deg C
Box_PV_temp = round(get_TempSensorVal(PV_temp_R, 1) )
data_log_fn("Temp_data.csv",Box_PV_temp,"Box temp")

upload("Temp_data.csv")

# Close the SPI
spi.close()
