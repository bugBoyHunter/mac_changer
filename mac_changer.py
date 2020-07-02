#!/usr/bin/ python
#ether 00:0c:29:44:03:bc
import subprocess
import optparse

#mac changer
def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    print("*"*100)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# instructions
parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")

(options, arguments) = parser.parse_args()

#call function
change_mac(options.interface, options.new_mac)




