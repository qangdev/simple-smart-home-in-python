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
print("\n******************* REGSITRATION OF THE DEVICES THROUGH SERVER *******************")

print('\n******************* REGSITRATION OF LIGHT DEVICES INITIATED *******************')
light_device_1 = Light_Device("light_1", ROOM_KITCHEN)
time.sleep(WAIT_TIME)
print('\n')
light_device_2 = Light_Device("light_2", ROOM_LIVING)
time.sleep(WAIT_TIME)
print('\n')
light_device_3 = Light_Device("light_3", ROOM_LIVING)
time.sleep(WAIT_TIME)
print('\n')
light_device_4 = Light_Device("light_4", ROOM_BED)
time.sleep(WAIT_TIME)
print('\n')
light_device_5 = Light_Device("light_5", ROOM_BED)
time.sleep(WAIT_TIME)
print('\n')

print('\n******************* REGSITRATION OF AC DEVICES INITIATED *******************')
# Creating the ac_device
ac_device_1 = AC_Device("ac_1", ROOM_KITCHEN)
time.sleep(WAIT_TIME)
ac_device_2 = AC_Device("ac_2", ROOM_LIVING)
time.sleep(WAIT_TIME)
ac_device_3 = AC_Device("ac_3", ROOM_BED)
time.sleep(WAIT_TIME)

print('\n******************* REGSITRED DEVICES ON THE SERVER *******************')
print('\nFetching the list of registered devices from EdgeServer')
print('\nThe Registered devices on Edge-Server:')
print(edge_server_1.get_registered_device_list())


print('\n******************* GETTING THE STATUS AND CONTROLLING THE DEVICES *******************')
cmd_counter = 1
# Get status from all connected devices

print("\n******************* GETTING THE STATUS BY DEVICE ID *******************")
units = ['light_1', 'light_2', 'light_3', 'light_4', 'light_5', 'ac_1', 'ac_2', 'ac_3']
for unit in units:
    print(f"Status based on device_id: {unit}")
    print(f"Command ID {cmd_counter} request is intiated.")
    status = edge_server_1.get_status(unit=unit)
    print(f"Here is the current device-status for {unit}", status)
    print(f"Command ID {cmd_counter} is executed.")
    cmd_counter += 1

print("\n******************* GETTING THE STATUS BY DEVICE_TYPE *******************")
device_types = ['LIGHT', 'AC']
for device_type in device_types:
    print(f"Status based on device type: {device_type}")
    print(f"Command ID {cmd_counter} request is intiated.")
    objs = edge_server_1.get_status(device_type=device_type)
    for obj in objs:
        print(f"Here is the current device-status for {obj['device_id']}", obj)
    print(f"Command ID {cmd_counter} is executed.")
    cmd_counter += 1


print("\n******************* GETTING THE STATUS BY ROOM TYPE *******************")
room_types = [ROOM_BED, ROOM_KITCHEN, ROOM_LIVING]
for room_type in room_types:
    print(f"Status based on room: type: {room_type}")
    print(f"Command ID {cmd_counter} request is intiated.")
    objs = edge_server_1.get_status(room_type=room_type)
    for obj in objs:
        print(f"Here is the current device-status for {obj['device_id']}", obj)
    print(f"Command ID {cmd_counter} is executed.")
    cmd_counter += 1


print("\n******************* GETTING THE STATUS BY ENTIRE HOUSE *******************")
print(f"Status for entire house")
print(f"Command ID {cmd_counter} request is intiated.")
objs = edge_server_1.get_status()
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

print("\n******************* SETTING UP THE STATUS AND CONTROLLING BY DEVICE ID *******************")

print('Controlling the devices based on ID:', 'light_1')
print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(unit='light_1', switch_state="ON")
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

print('Controlling the devices based on ID:', 'ac_1')
print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(unit='ac_1', switch_state="ON")
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

print('Controlling the devices based on ID:', 'light_1')
print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(unit='light_1', intensity="MEDIUM")
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

'''
Adjust AC-1 temperature to 29C 
'''
print('Controlling the devices based on ID:', 'ac_1')
print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(unit='ac_1', temperature=29)
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

'''
Adjust Light-2 intensity to HIGH 
'''
print('Controlling the devices based on ID:', 'light_2')
print(f'Command ID {cmd_counter} request is initiated.')
obj = edge_server_1.set(unit='light_2', intensity='HIGH')
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

print('******************* SETTING UP THE STATUS AND CONTROLLING BY THE DEVICE TYPE *******************')
print('> Turn all AC-* on')
print(f'Controlling the devices based on TYPE: {DEVICE_TYPE_AC}')
print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(device_type=DEVICE_TYPE_AC, switch_state='ON')
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

print('> Adjust all AC-* temperature to 21C')
print(f'Controlling the devices based on TYPE: {DEVICE_TYPE_AC}')
print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(device_type=DEVICE_TYPE_AC, temperature='21')
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

print('> Turn all Light-* on')
print(f'Controlling the devices based on TYPE: {DEVICE_TYPE_LIGHT}')
print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(device_type=DEVICE_TYPE_LIGHT, switch_state='ON')
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

print('> Adjust all Light-* intensity to MEDIUM')
print(f'Controlling the devices based on TYPE: {DEVICE_TYPE_AC}')
print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(device_type=DEVICE_TYPE_AC, intensity='MEDIUM')
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

print('******************* SETTING UP THE STATUS AND CONTROLLING BY ROOM *******************')
print('> Adjust all AC-* in the KITCHEN temperature to 30C')
print(f'Controlling the devices based on TYPE: {ROOM_KITCHEN}')
print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(room_type=ROOM_KITCHEN, temperature='30')
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

print('> Adjust all AC-* in BED-ROOM temperature to 29C')
print(f'Controlling the devices based on TYPE: {ROOM_BED}')
print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(room_type=ROOM_BED, temperature='28')
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

print('******************* SETTING UP THE STATUS AND CONTROLLING FOR ENTIRE HOUSE *******************')
print('> Turn all AC-* off')
print(f'Controlling the devices for the entire hourse')
print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(switch_state="OFF")
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

print('******************* SETTING UP THE STATUS AND CONTROLLING FOR INVALID REQUESTS *******************')
print('> Set an invalid value for Light-1 intensity')
print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(unit='light_1', intensity="MAX")
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

print('> Set an invalid value for Light-1 intensity')
print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(unit='light_1', intensity="MIN")
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

print('> Set an invalid value for AC-1 temperature')
print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(unit='ac_1', temperature="10")
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

print('> Set an invalid value for AC-1 temperature')
print(f'Command ID {cmd_counter} request is initiated.')
objs = edge_server_1.set(unit='ac_1', temperature="HOT")
for obj in objs:
    print(f"Here is the current device-status for {obj['device_id']}", obj)
print(f"Command ID {cmd_counter} is executed.")
cmd_counter += 1

print("\nSmart Home Simulation stopped.")
edge_server_1.terminate()
