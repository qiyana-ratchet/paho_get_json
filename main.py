import paho.mqtt.client as mqtt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("arduino-capstone-firebase-adminsdk-lnsjg-e680b65d57.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://arduino-capstone-default-rtdb.asia-southeast1.firebasedatabase.app/'})

soundDB = db.reference()

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
    url = "http://127.0.0.1:5000"
    soundDB.update({'sound1': str(msg.payload.decode("utf-8"))})
    soundDB.update({'sound2': str(msg.payload.decode("utf-8"))})
    soundDB.update({'sound3': str(msg.payload.decode("utf-8"))})
    soundDB.update({'sound4': str(msg.payload.decode("utf-8"))})
    soundDB.update({'sound5': str(msg.payload.decode("utf-8"))})
    soundDB.update({'sound6': str(msg.payload.decode("utf-8"))})

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

