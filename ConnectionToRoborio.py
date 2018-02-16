import sys
import time
from networktables import NetworkTables
import logging


roborioAddress = 'roborio-4132-FRC.local'
networkTableName = 'roborioDatatable'

fileName = 'androidOutputFile'
createFileCommand = '<some command must go here>'

NetworkTables.initialize(server = roborioAddress)
table = NetworkTables.getTable(networkTableName)

outputFile = open(fileName, 'r')

            
i = 0
while True:
    #run os commands to create output file from android
    os.system(createFileCommand)

    #read file
    rawOutputData = outputFile.read()

    #probably do something to correctly format raw output data
    
    #send to roborio
    table.putNumber('raspiData', rawOutputData)



