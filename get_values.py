from os import system

import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

if humidity is not None and temperature is not None:
    print("T={0:0.1f}*C H={1:0.1f}%".format(temperature, humidity))
else:
    print("Failed to retrieve data from sensor...")
