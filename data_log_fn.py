import csv
from millis import current_milli_time


def data_log_fn (filename,value,sensor_info):
    

        log = open(filename, "a")
        writer = csv.writer(log,delimiter=",")
        print writer
        enties = sensor_info+"#"+str(current_milli_time())+"#"+str(0)+"#"+str(value)
        enties = enties.split("#")
        print enties
        writer.writerow(enties)
        log.close()
         
