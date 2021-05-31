# Created by Sezer BOZKIR<admin@sezerbozkir.com> at 31.05.2021
import random
import paho.mqtt.client as paho
from time import sleep


def on_connect(client, userdata, flags, rc):
    print(f"Connack received with code f{rc}")


def on_publish(client, userdata, mid):
    print(f"mid: {mid}")


if __name__ == '__main__':
    client = paho.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect("localhost", 1883)

    while True:
        temperature = random.randint(1, 100)
        (rc, mid) = client.publish("sample/temperature", str(temperature), qos=1)
        print(rc)
        print(mid)
        sleep(5)
