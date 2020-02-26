from os import system
from tkinter import *

import Adafruit_DHT
import time, threading, schedule

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def getTempAndHumidity():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return humidity, temperature
    else:
        return None

root = Tk()

readings = tuple()
temp = StringVar()
hum = StringVar()
temp.set("TEMP")
hum.set("HUM")

def updateReadings():
#    while True:
        readings = getTempAndHumidity()
        hum.set("{0:0.1f}%".format(readings[0]))
        temp.set("{0:0.1f}*C".format(readings[1]))
        print("Updated!")
 #       time.sleep(5)

Label(root,textvariable=temp).grid(row=0, column=1)
Label(root,textvariable=hum).grid(row=1, column=1)
Label(root, text="Tempterature:").grid(row=0, column=0)
Label(root, text="Humidity:").grid(row=1, column=0)

updateReadings()
#schedule.every(5).seconds.do(updateReadings)
#threading.Thread(target=updateReadings, daemon=True).start()

mainloop()
