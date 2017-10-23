# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:24:24 2017

@author: sripals
"""

def get_TempSensorVal(res_rx,sensor_ref):
   
    import numpy as N

    Senor_temp = 0
    location = 0
    res_rx = res_rx/1000
    if(sensor_ref == 01):
        data = N.loadtxt('Free_Temp_lookup_table.txt',delimiter="\t",dtype=None,ndmin =2)
    elif (sensor_ref ==02):
        data = N.loadtxt('Paid_Temp_lookup_table.txt',delimiter="\t",dtype=None,ndmin =2)
    else:
        data =0
    size= N.shape(data)
    max_row = size[0]
    
    for i in range(max_row - 1):
        
        if ( (res_rx < data[i+1][1]) and (res_rx > data[i][1])):
           location = i
    
    T2 = data[location+1][0]
    T1 = data[location-1][0]
    R2 = data[location+1][1]
    R1 = data[location-1][1]
#    print T1
#    print T2
#    print R1
#    print R2
    slope = (T1-T2)/(R2-R1)
    
    if res_rx > data[location][1]:
        delta_res = res_rx-data[location][1]
    else: 
        delta_res = data[location][1]-res_rx
    
    
    Senor_temp = (slope*(delta_res)+data[location][0])
    return (Senor_temp)

    
