import sys
import time
import os
from networktables import NetworkTables
import logging


roborioAddress = 'roborio-4132-FRC.local'
networkTableName = 'roborioDatatable'

fileName = 'info.txt'
createFileCommand = 'adb pull storage/emulated/0/Notes/info.txt /home/pi/Documents/Github/PyToRoborio'

NetworkTables.initialize(server = roborioAddress)
table = NetworkTables.getTable(networkTableName)

#for testing
testArray = [1,2,3,4,5,6,7,8,9]




lastRawOutputData = ""
            
i = 0
while True:
    #runs os commands
    os.system(createFileCommand)

    rawOutputData = ""
    rawLineOutputData = ""
    outputFile = open(fileName, 'r')

    
    
   
    #read file
    rawOutputLineData = outputFile.read()
    while ( rawOutputLineData != ""):
	rawOutputData = rawOutputData + str(rawOutputLineData)
	rawOutputLineData = outputFile.read()	

    #probably do something to correctly format raw output data
    
    #send to roborio
    #table.putNumber('raspiData', rawOutputData)


    #if there's any changes print last data
    if (rawOutputData != lastRawOutputData): 
        print("Raw Output Data: " + rawOutputData)

    lastRawOutputData = rawOutputData

    #testing
    table.putNumberArray("testNumArray", testArray)

    



