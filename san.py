#!/usr/bin/python

from netmiko import ConnectHandler

net_connect = ConnectHandler(device_type='huawei', ip='192.168.30.61', username='admin', password='Admin@storage')

output = net_connect.send_command("showalarm")

print output

net_connect.disconnect()
