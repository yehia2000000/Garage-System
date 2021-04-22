#library to get reading from switches

#importing module for GPIO initialization
from machine import Pin

#Pins of 3 push buttons
Inc_pin = 25
Dec_pin = 26
Res_pin = 27
#Pin of on/off switch
Tog_pin = 35

#initializing all previous pins as input and pullup
Inc = Pin(Inc_pin, Pin.IN, Pin.PULL_UP)
Dec = Pin(Dec_pin, Pin.IN, Pin.PULL_UP)
Reset = Pin(Res_pin, Pin.IN, Pin.PULL_UP)
Toggle = Pin(Tog_pin, Pin.IN, Pin.PULL_UP)

#initializing variables for switch debouncing
Debounce1=0
Debounce2=0

#function to get key status
def GetKeyStatus():
    Time =200 #Debounce Time
    key = [0,0,0] #list contanining status of 3 push buttons , to be returned in the end of the function
    #it returns 0 if not pressed and 1 if pressed
    #key[0] -> Increment Signal
    #key[1] -> Decrement Signal
    #key[2] -> Reset Signal
    
    #making the variables in the global scope
    global Debounce1
    global Debounce2
    
    #check if reset button is pressed
    if (Reset.value()==0):
        key[2]=1
        
    #Check if increment button is pressed and implementing debouncing algorithm
    if (Inc.value()==0):
        Debounce1+=1
    else:
        Debounce1=0
    
    #Check if decrement button is pressed and implementing debouncing algorithm
    if (Dec.value()==0):
        Debounce2+=1
    else:
        Debounce2=0
    
    #Taking action if only button debounce counter reaches debounce time
    if(Debounce1>Time):
        Debounce1=0
        key[0]=1
    
    #Taking action if only button debounce counter reaches debounce time
    if(Debounce2>Time):
        Debounce2=0
        key[1]=1
    
    #returning the list containing the status of 3 push buttons
    return key

#function to get the value of the on/off switch
def GetToggleValue():
    return Toggle.value()
        