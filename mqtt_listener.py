import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"📩 Alert received: {message.payload.decode()}")

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)

client.subscribe("cmp4221/yolo/alerts")
client.on_message = on_message

client.loop_forever()
