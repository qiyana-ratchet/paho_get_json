from datetime import datetime

import paho.mqtt.client as mqtt
import firebase_admin
from firebase_admin import firestore, credentials

cred = credentials.Certificate("sungwonarduino-firebase-adminsdk-py0cm-ec2835c5c8.json")
firebase_admin.initialize_app(cred)
# Application Default credentials are automatically created.
db = firestore.client()

###########################################
url = "http://127.0.0.1:5000/"


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

    # soundDB.update({'sound1': str(msg.payload.decode("utf-8"))})
    # soundDB.update({'sound2': str(msg.payload.decode("utf-8"))})
    # soundDB.update({'sound3': str(msg.payload.decode("utf-8"))})
    # soundDB.update({'sound4': str(msg.payload.decode("utf-8"))})
    # soundDB.update({'sound5': str(msg.payload.decode("utf-8"))})
    # soundDB.update({'sound6': str(msg.payload.decode("utf-8"))})

    # r = requests.post(url, data={'id': 'ksg', 'pw': 'password!@#'})
    # print(r.status)
    # print(r.text)


# 새로운 클라이언트 생성
client = mqtt.Client()
# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_subscribe(topic 구독),
# on_message(발행된 메세지가 들어왔을 때)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message
# address : localhost, port: 1883 에 연결
client.connect('broker.mqttdashboard.com', 1883)
# common topic 으로 메세지 발행
client.subscribe('classTopic', 1)
client.loop_forever()
