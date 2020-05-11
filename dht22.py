from os import system

import Adafruit_DHT
from time import sleep

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def continuous_print():
    try:
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            if humidity is not None and temperature is not None:
                #system('clear')
                print("T={0:5.1f}*C H={1:5.1f}%".format(temperature, humidity))
            else:
                print("Failed to retrieve data from sensor...")
            sleep(2)
    except KeyboardInterrupt:
        print("Exiting...")

def get_values():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return (humidity, temperature)
    else:
        print("get_values: fetch error")
        return None

if __name__ == "__main__":
    continuous_print()
