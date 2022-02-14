import time
from Topics import Topic
from EdgeServer import Edge_Server
from LightDevice import Light_Device
from ACDevice import AC_Device

WAIT_TIME = 0.25



print("\nSmart Home Simulation started.")
# Creating the edge-server for the communication with the user

edge_server_1 = Edge_Server(instance_name='edge_server_1')
time.sleep(WAIT_TIME)  

# Creating the light_device
print("Intitate the device creation and registration process." )
print("\nCreating the Light devices for their respective rooms.")
light_device_1 = Light_Device("light_1", "Kitchen")
time.sleep(WAIT_TIME)
light_device_2 = Light_Device("light_2", "Kitchen")
time.sleep(WAIT_TIME)

# # Creating the ac_device  
# print("\nCreating the AC devices for their respective rooms. ")
# ac_device_1 = AC_Device("ac_1", "BR1")
# time.sleep(WAIT_TIME)

# Get status from all connected devices
print(edge_server_1.get_status())

print("\nSmart Home Simulation stopped.")
edge_server_1.terminate()
