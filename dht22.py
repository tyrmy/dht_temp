import Adafruit_DHT
from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def continuous_print():
    try:
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            if humidity is not None and temperature is not None:
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

def print_to_lcd():
    lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=6, d6=5, d7=21, cols=16, lines=2)
    try:
        while True:
            lcd.clear()
            hum, temp = get_values()
            print(hum, temp)
            lcd.set_cursor(0,0)
            lcd.message("Temp: {0:.2f} C".format(temp))
            lcd.set_cursor(0,1)
            lcd.message("Humi: {0:.2f} %".format(hum))
            sleep(2)
    except KeyboardInterrupt:
        print('Exiting...')
        lcd.clear()
        lcd.set_cursor(0,0)
        lcd.message("Offline")

if __name__ == "__main__":
    #continuous_print()
    print_to_lcd()
