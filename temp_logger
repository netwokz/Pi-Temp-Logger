__author__ = 'netwokz'

# Raspberry Pi Temperature Logger
# Stephen M Deane Jr
# www.thepowerofpi.com
# 6/5/2015

import time
import datetime


def temperature():
    temp = 32
    return temp


print("Temperature Data Logger\n")

while True:
    # Open Log File
    f = open('tempdata.txt', 'a')
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y/%m/%d %H:%M")
    outvalue = temperature()
    outstring = str(timestamp) + "  " + str(outvalue) + " C " + str(outvalue * 1.8 + 32) + " F" + "\n"
    print outstring
    f.write(outstring)
    f.close()

    # log temperature every 60 seconds
    time.sleep(60)
