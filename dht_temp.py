from os import system

import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

print('Tämä om Raspberry Pi -pohjainen lämpötilamittariohjelma. Käytössä on DHT22 mittari, jolta vastaanotetaan dataa joka toinen sekunti. \n\n Ohjelma alkaa aivan kohta...')

time.sleep(5)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        system('clear')
        print("Temp={0:0.1f}*C \nHumidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from sensor...")

    time.sleep(2)
