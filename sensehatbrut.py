from sense_hat import SenseHat

sense = SenseHat()

humidity = round(sense.get_humidity(),2)
temp = round(sense.get_temperature(),2)
pressure = round(sense.get_pressure(),2)
north = round(sense.get_compass(),2)

print (humidity)
print (temp)
print (pressure)
print (north)
