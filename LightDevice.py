from email import message
import json
import paho.mqtt.client as mqtt

from Topics import Topic

HOST = "localhost"
PORT = 1883


class Light_Device():
    
    # setting up the intensity choices for Smart Light Bulb  
    _INTENSITY = ["OFF", "LOW", "HIGH", "MEDIUM"]

    TOPIC_ACKNOWNLEDGEMENT = []
    TOPIC_STATUS = []
    TOPIC_CONTROLLING_STATE = []
    TOPIC_CONTROLLING_INTENSITY = []

    def __init__(self, device_id, room):
        # Assigning device level information for each of the devices. 
        self._device_id = device_id
        self._room_type = room
        self._light_intensity = self._INTENSITY[0]
        self._device_type = "LIGHT"
        self._device_registration_flag = False
        self._topics = set()
        self.client = mqtt.Client(self._device_id)  
        self.client.on_connect = self._on_connect  
        self.client.on_message = self._on_message  
        self.client.on_disconnect = self._on_disconnect  
        self.client.connect(HOST, PORT, keepalive=60)  
        self.client.loop_start()
        self._register_device(self._device_id, self._room_type, self._device_type)
        self._switch_status = "OFF"
    
    def _register_device(self, device_id, room_type, device_type):
        # During creation of the device, implement a call to the server to register itself
        payload = {
            'device_id': device_id,
            'device_type': device_type,
            'room_type': room_type
        }
        self.client.publish(
            Topic.REGISTRATION,
            payload=json.dumps(payload)
        )

    # Connect method to subscribe to various topics. 
    def _on_connect(self, client, userdata, flags, result_code):
        # Subscribe to topics once the device is connected to MQTT broker
        '''
        Topics are grouped into sub-topics
        '''
        self.TOPIC_ACKNOWNLEDGEMENT = [
            f'devices/acknownledgement/{self._device_id}'
        ]
        self.TOPIC_STATUS = [
            f'devices/{self._device_id}/status',
            f'devices/{self._device_type}/status',
            f'devices/{self._room_type}/status',
            f'devices/all/status'
        ]
        self.TOPIC_CONTROLLING_STATE = [
            f'devices/{self._device_id}/state',
            f'devices/{self._device_type}/state',
            f'devices/{self._room_type}/state',
            f'devices/all/state'
        ]
        self.TOPIC_CONTROLLING_INTENSITY = [
            f'devices/{self._device_id}/intensity',
            f'devices/{self._device_type}/intensity',
            f'devices/{self._room_type}/intensity',
            f'devices/all/intensity'
        ]
        self._subscribe_topics()

    # method to process the recieved messages and publish them on relevant topics 
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg):
        if msg.topic in self.TOPIC_ACKNOWNLEDGEMENT:
            obj = json.loads(msg.payload)
            print(f"LIGHT-DEVICE Registered! - Registration status is available for '{self._device_id}': {obj['status']}")
        elif msg.topic in self.TOPIC_STATUS:
            self.client.publish(
                f"devices/status",
                payload=json.dumps(self.get_current_status())
            )
        elif msg.topic in self.TOPIC_CONTROLLING_STATE:
            obj = json.loads(msg.payload)
            self._set_switch_status(obj["switch_state"])
            self.client.publish(
                f"devices/status",
                payload=json.dumps(self.get_current_status())
            )
        elif msg.topic in self.TOPIC_CONTROLLING_INTENSITY:
            obj = json.loads(msg.payload)
            self._set_light_intensity(obj["intensity"])
            self.client.publish(
                f"devices/status",
                payload=json.dumps(self.get_current_status())
            )

    def _subscribe_topics(self):
        for topic in self.TOPIC_ACKNOWNLEDGEMENT + self.TOPIC_STATUS + self.TOPIC_CONTROLLING_INTENSITY + self.TOPIC_CONTROLLING_STATE:
            self.client.subscribe(topic)

    def _on_disconnect(self, client, userdata, rc):
        pass

    # Getting the current switch status of devices 
    def _get_switch_status(self):
        return self._switch_status

    # Setting the the switch of devices
    def _set_switch_status(self, switch_state):
        self._switch_status = switch_state

    # Getting the light intensity for the devices
    def _get_light_intensity(self):
        return self._light_intensity

    # Setting the light intensity for devices
    def _set_light_intensity(self, light_intensity):
        self._light_intensity = light_intensity    

    def get_current_status(self):
        return {
            "device_id": self._device_id,
            'switch_state': self._get_switch_status(), 
            'intensity': self._get_light_intensity()
        }