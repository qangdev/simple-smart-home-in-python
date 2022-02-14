
import json
import time
import paho.mqtt.client as mqtt
 
from Topics import Topic


HOST = "localhost"
PORT = 1883     
WAIT_TIME = 0.25  

class Edge_Server:
    
    def __init__(self, instance_name):
        self._instance_id = instance_name
        self.client = mqtt.Client(self._instance_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.connect(HOST, PORT, keepalive=60)
        self.client.loop_start()
        self._registered_list = []
        self._topics = set()

    # Terminating the MQTT broker and stopping the execution
    def terminate(self):
        self.client.disconnect()
        self.client.loop_stop()

    # Connect method to subscribe to various topics.     
    def _on_connect(self, client, userdata, flags, result_code):
        # Subscribe topics once the server is connected to MQTT borker then sub
        self._subscribe_topics()
    
    # method to process the recieved messages and publish them on relevant topics 
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg):
        if msg.topic == Topic.REGISTRATION_REQ:
            device = json.loads(msg.payload)
            print(f"Registration request is acknowledged for device '{device['device_id']}' in {device['room_type']}")
            print(f"Request is processed for {device['device_id']}.")
            self._resgister_device(device)
        elif msg.topic == Topic.STATUS_RESP:
            resp = json.loads(msg.payload)
            print(f"Here is the current device-status for {resp['device_id']}: {resp}")

    def _subscribe_topics(self):
        self._topics = {
            Topic.REGISTRATION_REQ,
            Topic.STATUS_RESP
        }
        for topic in self._topics:
            self.client.subscribe(topic)
        # print(f"{self._instance_id} subscribes to {self._topics}")

    def _resgister_device(self, device):
        self._registered_list.append(device)
        self.client.publish(
            f"{Topic.REGISTRATION_RESP}/{device['device_id']}",
            payload=json.dumps({
                "status": device in self._registered_list 
            })
        )

    # Returning the current registered list
    def get_registered_device_list(self):
        return self._registered_list

    # Getting the status for the connected devices
    # question 2a
    def get_status(self):
        self.client.publish(
            Topic.STATUS_REQ
        )
        time.sleep(WAIT_TIME)
        return self._registered_list

    # Controlling and performing the operations on the devices
    # based on the request received
    def set(self):
        pass
