import cmd
import time
from EdgeServer import Edge_Server
from LightDevice import Light_Device
from ACDevice import AC_Device

WAIT_TIME = 0.25

# Contant names are a little backward but it helps to make them more consistency and easy to remember
'''
ROOM_*:
'''
ROOM_KITCHEN = 'KITCHEN'
ROOM_LIVING = 'LIVING'
ROOM_BATH = "BATH"
ROOM_BED = "BED"

'''
DEVICE_TYPE_*
'''
DEVICE_TYPE_LIGHT = "LIGHT"
DEVICE_TYPE_AC = "AC"

print("\nSmart Home Simulation started.")
# Creating the edge-server for the communication with the user

edge_server_1 = Edge_Server(instance_name='edge_server_1')
time.sleep(WAIT_TIME)  

# Creating the light_device
print("Intitate the device creation and registration process." )
print("\nCreating the Light devices for their respective rooms.")
print("******************* REGSITRATION OF THE DEVICES THROUGH SERVER *******************")
light_device_1 = Light_Device("light_1", ROOM_KITCHEN)
time.sleep(WAIT_TIME)
light_device_2 = Light_Device("light_2", ROOM_LIVING)
time.sleep(WAIT_TIME)
light_device_3 = Light_Device("light_3", ROOM_LIVING)
time.sleep(WAIT_TIME)
light_device_4 = Light_Device("light_4", ROOM_BED)
time.sleep(WAIT_TIME)
light_device_5 = Light_Device("light_5", ROOM_BED)
time.sleep(WAIT_TIME)


ac_device_1 = AC_Device("ac_1", ROOM_KITCHEN)
time.sleep(WAIT_TIME)
ac_device_2 = AC_Device("ac_2", ROOM_LIVING)
time.sleep(WAIT_TIME)
ac_device_3 = AC_Device("ac_3", ROOM_LIVING)
time.sleep(WAIT_TIME)
ac_device_4 = AC_Device("ac_4", ROOM_BED)
time.sleep(WAIT_TIME)
ac_device_5 = AC_Device("ac_5", ROOM_BED)
time.sleep(WAIT_TIME)

# # Creating the ac_device  
# print("\nCreating the AC devices for their respective rooms. ")
# ac_device_1 = AC_Device("ac_1", "BR1")
# time.sleep(WAIT_TIME)
# print("\n")
cmd_counter = 1
# Get status from all connected devices

# print("******************* GETTING THE STATUS BY DEVICE_ID *******************")
# for device in edge_server_1.get_registered_device_list():
#     print(f"Status based on device_id: {device['device_id']}")
#     print(f"Command ID {cmd_counter} request is intiated.")
#     status = edge_server_1.get_status(unit=device['device_id'])
#     print(f"Here is the current device-status for {device['device_id']}", status)
#     print(f"Command ID {cmd_counter} is executed.")
#     cmd_counter += 1

# print("******************* GETTING THE STATUS BY DEVICE_TYPE *******************")
# device_types = {device["device_type"] for device in edge_server_1.get_registered_device_list()}
# for device_type in device_types:
#     print(f"Status based on device type: {device_type}")
#     print(f"Command ID {cmd_counter} request is intiated.")
#     objs = edge_server_1.get_status(device_type=device_type)
#     for obj in objs:
#         print(f"Here is the current device-status for {obj['device_id']}", obj)
#     print(f"Command ID {cmd_counter} is executed.")
#     cmd_counter += 1


# print("******************* GETTING THE STATUS BY ROOM_TYPE *******************")
# room_types = {device["room_type"] for device in edge_server_1.get_registered_device_list()}
# for room_type in room_types:
#     print(f"Status based on room: type: {room_type}")
#     print(f"Command ID {cmd_counter} request is intiated.")
#     objs = edge_server_1.get_status(room_type=room_type)
#     for obj in objs:
#         print(f"Here is the current device-status for {obj['device_id']}", obj)
#     print(f"Command ID {cmd_counter} is executed.")
#     cmd_counter += 1


# print("******************* GETTING THE STATUS BY ENTIRE_HOME *******************")
# print(f"Status entire home")
# print(f"Command ID {cmd_counter} request is intiated.")
# objs = edge_server_1.get_status()
# for obj in objs:
#     print(f"Here is the current device-status for {obj['device_id']}", obj)
# print(f"Command ID {cmd_counter} is executed.")
# cmd_counter += 1

# print("******************* SETTING UP THE STATUS AND CONTROLLING THE DEVICE_ID *******************")
# for device in edge_server_1.get_registered_device_list():
#     print('Controlling the devices based on ID:', device['device_id'])
#     print(f'Command ID {cmd_counter} request is initiated.')
#     objs = edge_server_1.set(unit=device['device_id'], switch_state="ON")
#     for obj in objs:
#         print(f"Here is the current device-status for {obj['device_id']}", obj)
#     print(f"Command ID {cmd_counter} is executed.")
#     cmd_counter += 1

# print('******************* SETTING UP THE STATUS AND CONTROLLING BY THE DEVICE_TYPE *******************')
# print(f'Controlling the devices based on TYPE: {DEVICE_TYPE_LIGHT}')
# print(f'Command ID {cmd_counter} request is initiated.')
# objs = edge_server_1.set(device_type=DEVICE_TYPE_LIGHT, intensity="MEDIUM")
# for obj in objs:
#     print(f"Here is the current device-status for {obj['device_id']}", obj)
# print(f"Command ID {cmd_counter} is executed.")
# cmd_counter += 1

# print('******************* SETTING UP THE STATUS AND CONTROLLING BY ROOM *******************')
# print(f'Controlling the devices based on TYPE: {ROOM_KITCHEN}')

# print(f'Command ID {cmd_counter} request is initiated.')
# objs = edge_server_1.set(room_type=ROOM_KITCHEN, switch_state="OFF")
# for obj in objs:
#     print(f"Here is the current device-status for {obj['device_id']}", obj)
# print(f"Command ID {cmd_counter} is executed.")
# cmd_counter += 1

# print('******************* SETTING UP THE STATUS AND CONTROLLING FOR ENTIRE HOUSE *******************')
# print(f'Controlling the devices for the entire hourse')

# print(f'Command ID {cmd_counter} request is initiated.')
# objs = edge_server_1.set(switch_state="OFF")
# for obj in objs:
#     print(f"Here is the current device-status for {obj['device_id']}", obj)
# print(f"Command ID {cmd_counter} is executed.")
# cmd_counter += 1

# print('******************* CONTROLLING FOR ENTIRE HOUSE *******************')
# print(f'Controlling the devices for the entire hourse')

# print(f'Command ID {cmd_counter} request is initiated.')
# objs = edge_server_1.set(switch_state="OFF")
# for obj in objs:
#     print(f"Here is the current device-status for {obj['device_id']}", obj)
# print(f"Command ID {cmd_counter} is executed.")
# cmd_counter += 1

# print(f'Command ID {cmd_counter} request is initiated.')
# objs = edge_server_1.set(room_type=ROOM_KITCHEN, switch_state="TURNON")
# for obj in objs:
#     print(f"Here is the current device-status for {obj['device_id']}", obj)
# print(f"Command ID {cmd_counter} is executed.")
# cmd_counter += 1

# print(f'Command ID {cmd_counter} request is initiated.')
# objs = edge_server_1.set(room_type=ROOM_KITCHEN, intensity='MAX')
# for obj in objs:
#     print(f"Here is the current device-status for {obj['device_id']}", obj)
# print(f"Command ID {cmd_counter} is executed.")
# cmd_counter += 1

print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(unit='ac_1', temperature='99')
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1


print("\nSmart Home Simulation stopped.")
edge_server_1.terminate()
