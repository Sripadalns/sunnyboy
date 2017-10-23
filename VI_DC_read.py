from data_log_fn import data_log_fn
from ADC_SPI import *

# SPI channel 4 for DC Voltage
DC_V_chanl = 4

# SPI channel 5 for DC Current
DC_I_chanl = 5

# Pull up resistance for Sensor
R1 = 1000

#Reference ADC voltage. Need to read from GSM M66
Vref = 5

#ADC_SPI init
spi = MCP3208(0)

DC_V_count =  spi.read(DC_V_chanl)
DC_I_count =  spi.read(DC_I_chanl)

# Close SPI
spi.close()


DC_v = round ( (( DC_V_count* Vref)/float(4095)) ,3)
DC_v = (DC_v - 2.5) *500
DC_I = round ( (( DC_I_count* Vref)/float(4095)) ,3)
DC_I = (DC_I - 2.5) *40

data_log_fn("DC_Log.txt",DC_v,"DC Voltage")
data_log_fn("DC_Log.txt",DC_I,"DC current")
upload("DC_Log.txt")






