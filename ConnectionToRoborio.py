import sys
import time
from networktables import NetworkTables
import logging

class NetworkTableClient:
    i = 0;
    roborioAddress = 'roborio-4132-FRC.local'
    networkTableName = "roborioDatatable"
    
    NetworkTables.initialize(server = roborioAddress)
    table = NetworkTables.getTable(networkTableName)
    
    def run(self):
        while True:
            self.table.putNumber('robotTime', i)
            print(i)
            time.sleep(1)
            i += 1
            print(sd.getNumber('robotTime', 0))


