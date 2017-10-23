from data_log_fn import data_log_fn
import os


# read the text file AC_Log.txt
# Do the calculation
# Store Real Power and Reactive Power
realpower = 0
reactivepower = 0

data_log_fn("AC_Monitor.txt",realpower,"Real Power")
data_log_fn("AC_Monitor.txt",reactivepower,"Reactive Power")
upload("AC_Monitor.txt")

# delete AC_Log.txt
#os.remove("/home/sripals/Solar/Prod_v1/AC_Log.txt")




