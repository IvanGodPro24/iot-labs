import time
import json
import paho.mqtt.client as mqtt
from counterfit_shims_seeed_python_dht import DHT
from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5001)

sensor = DHT("11", 49)

id = '9c438157-4139-43ce-ad12-49a9e3482518'
client_name = id + 'temperature_sensor_client'
client_telemetry_topic = id + '/telemetry'

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

print("MQTT connected!")

while True:
    _, temp = sensor.read()
    telemetry = json.dumps({'temperature' : temp})

    print("Sending telemetry:", telemetry)

    mqtt_client.publish(client_telemetry_topic, telemetry)

    time.sleep(10 * 60)




