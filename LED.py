#library to activate Leds

#importing module for GPIO initialization
from machine import Pin

#Pins of 2 LEDs
Led1_pin = 13
Led2_pin = 2

#initializing all previous pins as output
Led1 = Pin(Led1_pin,Pin.OUT,value=0)
Led2 = Pin(Led2_pin,Pin.OUT,value=0)

#function to turn on first Led
def On1():
    Led1.on()

#function to turn off first Led
def Off1():
    Led1.off()
    
#function to turn on second Led
def On2():
    Led2.on()

#function to turn off second Led
def Off2():
    Led2.off()
      