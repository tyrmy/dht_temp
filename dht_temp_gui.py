from tkinter import *
import Adafruit_DHT

class tempApp():
    def __init__(self):
        self.root = Tk()
        self.temperatureLabel = Label(text="TEM")
        self.humidityLabel = Label(text="HUM")
        self.hum = Label(text="Humidity:")
        self.tem = Label(text="Temperature:")

        self.temperatureLabel.grid(row=0, column=1)
        self.humidityLabel.grid(row=1,column=1)
        self.tem.grid(row=0, column=0)
        self.hum.grid(row=1,column=0)

        self.updateValues()
        self.root.mainloop()

    def updateValues(self):
        DHT_SENSOR = Adafruit_DHT.DHT22
        DHT_PIN = 4

        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            self.humidityLabel.configure(text="{0:0.1f}%".format(humidity))
            self.temperatureLabel.configure(text="{0:0.1f}*C".format(temperature))
        else:
            self.humidityLabel.configure(text="...")
            self.temperatureLabel.configure(text="...")
        self.root.after(3000, self.updateValues)

app = tempApp()
