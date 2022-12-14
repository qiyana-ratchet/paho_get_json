from datetime import datetime
import paho.mqtt.client as mqtt
import firebase_admin
from firebase_admin import firestore, credentials

cred = credentials.Certificate("sungwonarduino-firebase-adminsdk-py0cm-ec2835c5c8.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    print(str(msg.payload.decode("utf-8")))
    now = datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    db.collection('data').document('mat1').set({
        'value': str(msg.payload.decode("utf-8")),
        'time': now.strftime('%Y-%m-%d %H:%M:%S'),
        'TagSnapshot': "1",
        'SensorTag': "1",
    })
    db.collection('data').document('mat2').set({
        'value': str(msg.payload.decode("utf-8")),
        'time': now.strftime('%Y-%m-%d %H:%M:%S'),
        'TagSnapshot': "1",
        'SensorTag': "2",
    })
    db.collection('data').document('mat3').set({
        'value': str(msg.payload.decode("utf-8")),
        'time': now.strftime('%Y-%m-%d %H:%M:%S'),
        'TagSnapshot': "1",
        'SensorTag': "3",
    })
    db.collection('data').document('mat4').set({
        'value': str(msg.payload.decode("utf-8")),
        'time': now.strftime('%Y-%m-%d %H:%M:%S'),
        'TagSnapshot': "1",
        'SensorTag': "4",
    })
    db.collection('data').document('mat5').set({
        'value': str(msg.payload.decode("utf-8")),
        'time': now.strftime('%Y-%m-%d %H:%M:%S'),
        'TagSnapshot': "1",
        'SensorTag': "5",
    })
    db.collection('data').document('mat6').set({
        'value': str(msg.payload.decode("utf-8")),
        'time': now.strftime('%Y-%m-%d %H:%M:%S'),
        'TagSnapshot': "1",
        'SensorTag': "6",
    })
    current_time = now.strftime('%Y-%m-%d %H:%M:%S')
    db.collection('timeData').document(current_time).set({
        'value': str(msg.payload.decode("utf-8")),
        'time': now.strftime('%Y-%m-%d %H:%M:%S'),
    })

client = mqtt.Client()  # ????????? ??????????????? ??????
client.on_connect = on_connect
# ?????? ?????? ?????? on_connect(???????????? ??????), on_disconnect(???????????? ????????????),
# on_subscribe(topic ??????), on_message(????????? ???????????? ???????????? ???)
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect('broker.mqttdashboard.com', 1883) # address : localhost, port: 1883 ??? ??????
client.subscribe('classTopic', 1) # classTopic ?????? ????????? ??????
client.loop_forever()
