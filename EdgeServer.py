
from itertools import count
import json
import time
import paho.mqtt.client as mqtt
from Topics import Topic



HOST = "localhost"
PORT = 1883     
WAIT_TIME = 0.5

class Edge_Server:

    TOPIC_STATUS = []
    TOPIC_EXCEPT = []
    TOPIC_REGISTRATION = []
    
    def __init__(self, instance_name):
        self._instance_id = instance_name
        self.client = mqtt.Client(self._instance_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.connect(HOST, PORT, keepalive=60)
        self.client.loop_start()
        self.devices_status = []
        self._registered_list = []

    # Terminating the MQTT broker and stopping the execution
    def terminate(self):
        self.client.disconnect()
        self.client.loop_stop()

    # Connect method to subscribe to various topics.     
    def _on_connect(self, client, userdata, flags, result_code):
        # Subscribe topics once the server is connected to MQTT borker then sub
        '''
        Topics are grouped into sub-topics
        '''
        self.TOPIC_REGISTRATION = [
            Topic.REGISTRATION
        ]
        self.TOPIC_STATUS = [
            Topic.RESPONSE_STATUS
        ]
        self.TOPIC_EXCEPT = [
            Topic.SETTING_EXCEPTION
        ]
        self._subscribe_topics()
    
    # method to process the recieved messages and publish them on relevant topics 
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg):
        if msg.topic in self.TOPIC_REGISTRATION:
            device = json.loads(msg.payload)
            print(f"Registration request is acknowledged for device '{device['device_id']}' in {device['room_type']}")
            print(f"Request is processed for {device['device_id']}.")
            self._resgister_device(device)
        elif msg.topic in self.TOPIC_STATUS:
            resp = json.loads(msg.payload)
            self.devices_status.append(resp)
        elif msg.topic in self.TOPIC_EXCEPT:
            resp = json.loads(msg.payload)
            print(resp['message'])

    def _subscribe_topics(self):
        for topic in self.TOPIC_STATUS + self.TOPIC_REGISTRATION + self.TOPIC_EXCEPT:
            self.client.subscribe(topic)

    def _resgister_device(self, device):
        self._registered_list.append(device)
        self.client.publish(
            Topic.ACKNOWNLEDGEMENT.format(target=device["device_id"])
        )

    # Returning the current registered list
    def get_registered_device_list(self):
        return self._registered_list

    # Getting the status for the connected devices
    def get_status(self, unit=None, device_type=None, room_type=None):
        '''
        Step 1: Clear old status
        '''
        self.devices_status = []

        '''
        Step 2: Get new status based on given param
        '''
        if unit:
            target = unit
        elif device_type:
            target = device_type
        elif room_type:
            target = room_type
        else:
            target = 'all'
        self.client.publish(Topic.REQUEST_STATUS.format(target=target))
        time.sleep(WAIT_TIME)
        
        return self.devices_status

    # Controlling and performing the operations on the devices
    # based on the request received
    def set(self, unit=None, device_type=None, room_type=None, 
            switch_state=None, intensity=None, temperature=None):
        '''
        Step 1: Clear old status
        '''
        self.devices_status = []

        '''
        Step 2: Publish request
        '''
        if unit:
            topic = f'devices/{unit}' 
        elif device_type:
            topic = f'devices/{device_type}'
        elif room_type:
            topic = f'devices/{room_type}'
        else:
            topic = f'devices/all'
        
        payload = {}
        if switch_state:
            topic += f'/state'
            payload["switch_state"] = switch_state
        elif intensity:
            topic += f'/intensity'
            payload["intensity"] = intensity
        elif temperature:
            topic += f'/temperature'
            payload["temperature"] = temperature

        self.client.publish(topic, payload=json.dumps(payload))
        time.sleep(WAIT_TIME)

        return self.get_status(unit=unit, device_type=device_type, room_type=room_type)
