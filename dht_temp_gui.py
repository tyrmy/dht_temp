from tkinter import *
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

class tempApp():
    def __init__(self):
        self.root = Tk()
        self.root.title("DHT22 Temperature App")
        self.temperatureLabel = Label(text="TEM")
        self.humidityLabel = Label(text="HUM")
        self.hum = Label(text="Humidity:")
        self.tem = Label(text="Temperature:")

        self.temperatureLabel.grid(row=0, column=2)
        self.humidityLabel.grid(row=1,column=2)
        self.tem.grid(row=0, column=1)
        self.hum.grid(row=1,column=1)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(3, weight=1)

        self.updateValues()
        #self.root.grid(sticky="nsew")
        self.root.minsize(300,100)

        self.root.mainloop()

    def updateValues(self):
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            self.humidityLabel.configure(text="{0:0.1f}%".format(humidity))
            self.temperatureLabel.configure(text="{0:0.1f}*C".format(temperature))
        else:
            self.humidityLabel.configure(text="...")
            self.temperatureLabel.configure(text="...")
        self.root.after(5000, self.updateValues)

app = tempApp()
