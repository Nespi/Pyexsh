from sense_hat import SenseHat
import time
import requests

sense = SenseHat()

def readings():
    humidity =str(round(sense.get_humidity(),2))
    temp = str(round(sense.get_temperature(),2))
    pressure = str(round(sense.get_pressure(),2))
    north = str(round(sense.get_compass(),1))
    url = 'https://dweet.io/dweet/for/sensehathtp?' + 'temp=' +temp + '&humidity=' + humidity + '&pressure=' + pressure
    r = requests.post(url)

while True:
    readings()
    time.sleep(30)
    print('Readings recorded')
