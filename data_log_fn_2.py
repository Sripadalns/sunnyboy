
import csv

log = open('try.csv', "a")
writer = csv.writer(log,delimiter=",")
enties = "PVPanle"+"#"+str(125)
enties = enties.split("#")
print enties
writer.writerow(enties)
log.close()
