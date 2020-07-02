#!/usr/bin/ python
#ether 00:0c:29:44:03:bc
import subprocess

interface = raw_input("interface > ")
new_mac = raw_input("new MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)
print("*"*100)
subprocess.call("ifconfig eth0", shell=True)
subprocess.call("ifconfig "+ interface +" down", shell=True)
subprocess.call("ifconfig "+ interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig "+ interface +" up", shell=True)
subprocess.call("ifconfig eth0", shell=True)