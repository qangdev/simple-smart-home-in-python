from email import message
import json
import paho.mqtt.client as mqtt

from Topics import Topic

HOST = "localhost"
PORT = 1883


class Light_Device():
    
    # setting up the intensity choices for Smart Light Bulb  
    _INTENSITY = ["OFF", "LOW", "HIGH", "MEDIUM"]

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
        self._subscribe_topics()

    # method to process the recieved messages and publish them on relevant topics 
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg):
        if msg.topic == f'{Topic.ACKNOWNLEDGEMENT}/{self._device_id}':
            resp = json.loads(msg.payload)
            print(f"LIGHT-DEVICE Registered! - Registration status is available for '{self._device_id}': {resp['status']}")
        
        # Server ask for specific status of all devices
        # Server ask for specific status of an device in a specific room type
        # Server ask for specific status of an device by specific device type
        # Server ask for specific status of an device by id
        if msg.topic in [
            f'devices/{self._device_id}/status',
            f'devices/{self._device_type}/status',
            f'devices/{self._room_type}/status',
            f'devices/all/status']:
            self.client.publish(
                f"devices/status",
                payload=json.dumps({
                    "device_id": self._device_id,
                    'switch_state': self._get_switch_status(), 
                    'intensity': self._get_light_intensity()
                })
            )

    def _subscribe_topics(self):
        self._topics = {
            f'devices/{self._device_id}/status',
            f'devices/{self._device_type}/status',
            f'devices/{self._room_type}/status',
            f'devices/all/status',
            f'{Topic.ACKNOWNLEDGEMENT}/{self._device_id}',
        }
        for topic in self._topics:
            self.client.subscribe(topic)

    def _on_disconnect(self, client, userdata, rc):
        pass

    # Getting the current switch status of devices 
    def _get_switch_status(self):
        return self._switch_status

    # Setting the the switch of devices
    def _set_switch_status(self, switch_state):
        pass

    # Getting the light intensity for the devices
    def _get_light_intensity(self):
        return self._light_intensity

    # Setting the light intensity for devices
    def _set_light_intensity(self, light_intensity):
        pass    
