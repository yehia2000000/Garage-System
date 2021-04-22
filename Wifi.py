#Library to establish Wifi connection

#importing module for network connection
import network

#initializing controller as an access point
wlan = network.WLAN(network.AP_IF)
#making wifi configurations
wlan.config(essid='Yehia')
wlan.config(max_clients=2)

#function to enable the Wifi connection
def Connect():
    wlan.active(True)
    print('network config:', wlan.ifconfig())

#function to disable the Wifi connection
def Disconnect():
    wlan.active(False)
    print('Disabling wifi')    