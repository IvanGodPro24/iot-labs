import time
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5001)

light_sensor = GroveLightSensor(49)

while True:
    light = light_sensor.light
    print('Light level:', light)
    time.sleep(1)