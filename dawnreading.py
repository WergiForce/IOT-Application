import json
import time
import schedule
from datetime import datetime, time, timedelta
from sense_hat import SenseHat
from urllib import urlopen

WRITE_API_KEY='GET-YOUR-OWN-API-KEY'

baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

sense = SenseHat()

def writeData(temp,press,hum):
    # Sending the data to thingspeak in the query string
    conn = urlopen(baseURL + '&field1=%s&field2=%s&field3=%s' % (temp,press,hum))
    print(conn.read())
    # Closing the connection
    conn.close()

def job():
    temp=round(sense.get_temperature(),2)
    press=round(sense.get_pressure(),2)
    hum=round(sense.get_humidity(),2)
    writeData(temp,press,hum) # After taking readings they are written to the thingspeak api

schedule.every().day.at("08:00").do(job) # Schedules reading for each morning at 08:00, so you can check and know how to dress or if you need to defrost the car

while True:
    schedule.run_pending()

