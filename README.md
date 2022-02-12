# simple-smart-home-in-python
Connecting devices to a center server using MQTT and python

# TODO:
1. [X] A class for TOPICS
2. [ ] How to get all status from connected devices

## To balance server and device load.
For registration and acknowlegdement: 
Single topic for registration but multilple topics for acknowlegdement

e.g: Server is running and it subscribe to `/registration/request` topic.Then *Light_1* device is added and it will send a registration request to the Server with same topic.
Then the server will catch that request and then append the device to its device list. Finally the server will send back to *Light_1* device an acknowlegdement response using a private topic just for that device by put the device's id to the topic `/registration/acknowledge/light_1`. 
*Light_1* also subscribe to `/registration/acknowledge/light_1` so it can receive the acknowlegdement from the server to indicate the connection between them is open.

## Resource
1. https://pypi.org/project/paho-mqtt/