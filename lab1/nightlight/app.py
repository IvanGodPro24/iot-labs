import paho.mqtt.client as mqtt
import time
import json
from counterfit_shims_grove.grove_led import GroveLed
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5001)

light_sensor = GroveLightSensor(49)
led = GroveLed(50)

id = 'e5402df2-7b4e-42bf-babe-1e64fb26ce45'
client_name = id + 'nightlight_client'
client_telemetry_topic = id + '/telemetry'
server_command_topic = id + '/commands'

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

def handle_command(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)
    
    if payload['led_on']:
        led.on()
    else:
        led.off()

mqtt_client.subscribe(server_command_topic)
mqtt_client.on_message = handle_command

print("MQTT connected!")

while True:
    light = light_sensor.light
    telemetry = json.dumps({'light': light})

    print("Sending telemetry:", telemetry)

    mqtt_client.publish(client_telemetry_topic, telemetry)

    time.sleep(5)