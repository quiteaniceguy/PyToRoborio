import sys
import time
from networktables import NetworkTables
import logging

NetworkTables.initialize(server = 'roborio-4132-FRC.local')

sd = NetworkTables.getTable("testDatatable")
i = 0
while True:
    sd.putNumber('robotTime', i)
    print(i)
    time.sleep(1)
    i += 1
    print(sd.getNumber('robotTime', 0))


