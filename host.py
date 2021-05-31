# Created by Sezer BOZKIR<admin@sezerbozkir.com> at 31.05.2021
import paho.mqtt.client as paho


def on_connect(client, userdata, flags, rc):
    print(f"Connack received with code f{rc}, f{client}, f{userdata}, f{flags}")


if __name__ == '__main__':
    client = paho.Client()
    client.on_connect = on_connect
    client.connect("localhost", 1883)
    client.loop_forever()
