#!/usr/bin/python

from netmiko import ConnectHandler

net_connect = ConnectHandler(device_type='huawei', ip='192.168.30.6', username='rootadmin', password='Huawei12#$')

net_connect.enter_config(huawei)

output = net_connect.send_command("vlan 666")

time.sleep(2)

output = net_connect.send_command("commit")

time.sleep(2)

output = net_connect.send_command("disp cu")

print output

net_connect.disconnect()
