#!/usr/local/bin/python

import time
import Adafruit_DHT

def get_weather():
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temp = Adafruit_DHT.read_retry(11, 18)

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).  
    # If this happens try again!
    if humidity is not None and temp is not None:
	#print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
        #Fahrenheit = 9.0/5.0 * Celcius + 32
        Fahrenheit = (temp * 1.8) + 32
        #print temperature, "C"
        #print Fahrenheit, "F"
	print "{:.0f}".format(Fahrenheit)
	print "{:.0f}".format(humidity)
	
    else:
	print "oops"      

def main():
    get_weather()

if __name__=='__main__':
    main()

