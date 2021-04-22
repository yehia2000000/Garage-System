#Library for timer initialization

#importing timer module from microcontroller
from machine import Timer

#Initializing Timer 0 
Send = Timer(0)

#initializing global function to be executed in ISR
def Global_Function():
    pass

#function to initialize timer
def Init(Timer_Callback):
    Send.init(period=500, mode=Timer.PERIODIC, callback=Timer_ISR) #initializing timer
    #callback function 
    global Global_Function
    Global_Function = Timer_Callback

#function to disable timer
def Disbale():
    Send.deinit()

#ISR function 
def Timer_ISR(timer):
    Global_Function()
