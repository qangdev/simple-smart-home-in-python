# simple-smart-home-in-python
Connecting devices to a center server using MQTT and python

# TODO:
1. [D] A class for TOPICS
2. [C] How to get all status from connected devices
3. [D] Watch http://www.steves-internet-guide.com/subscribing-topics-mqtt-client/
4. [D] Make topic constants for EdgeServer
5. [D] Controlling On/Off by ID
6. [D] Controlling On/Off by Device Type
7. [D] Controlling On/Off by Room Type
8. [D] Controlling On/Off for entire house
9. [D] Controlling Light intensity by ID
10. [D] Controlling Light intensity by Room Type
11. [D] Controlling Light intensity for entire house
12. [D] Get status AC by ID
13. [D] Get status AC by device type
14. [D] Get status AC by room type
15. [D] Get status AC for entire house 
16. [D] Controlling AC temperature by ID
17. [D] Controlling AC temperature by Room Type
18. [D] Controlling AC temperature for entire house
19. [ ] Make sample use cases
20. [ ] Update ReadMe to explain how this work
21. [ ] What to do on disconnection?
22. [ ] 


## Topics Design

To balance server and device load requesting topics from service to devices such as get current temperature of an AC. But there common topics for devices to send response to the server.
As the result devices won;t getting a lot of unnecessary information

For registration and acknowlegdement: 
Single topic for registration: `devices/registration`

But multilple topics for acknowlegdement: `devices/acknownledgement/<device_id>`


e.g: Server is running and it subscribe to `/registration/request` topic.Then *Light_1* device is added and it will send a registration request to the Server with same topic.
Then the server will catch that request and then append the device to its device list. Finally the server will send back to *Light_1* device an acknowlegdement response using a private topic just for that device by put the device's id to the topic `/registration/acknowledge/light_1`. 
*Light_1* also subscribe to `/registration/acknowledge/light_1` so it can receive the acknowlegdement from the server to indicate the connection between them is open.


## Use Cases
1. 
## Resource
1. https://pypi.org/project/paho-mqtt/
