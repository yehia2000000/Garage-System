#library for interrupt initialization 

#importing all switch information
from SW import *

#initializing global function to be executed in ISR of first interrupt
def Global_Function1():
    pass

#initializing global function to be executed in ISR of second interrupt
def Global_Function2():
    pass

#initializing global function to be executed in ISR of third interrupt
def Global_Function3():
    pass

#function for interrupt initialization
def Init(Inc_Callback, Dec_Callback, Res_Callback):
    #making functions in the global scope
    global Global_Function1
    global Global_Function2
    global Global_Function3
    
    #callback function
    Global_Function1 = Inc_Callback
    Global_Function2 = Dec_Callback
    Global_Function3 = Res_Callback
    
    #initialization of interrupts of 3 push buttons (falling edge)
    Inc.irq(trigger=Pin.IRQ_FALLING, handler=Inc_ISR)
    Dec.irq(trigger=Pin.IRQ_FALLING, handler=Dec_ISR)
    Reset.irq(trigger=Pin.IRQ_FALLING, handler=Res_ISR)

#function to disable interrupts
def Disable():
    Inc.irq(trigger=0, handler=Inc_ISR)
    Dec.irq(trigger=0, handler=Dec_ISR)
    Reset.irq(trigger=0, handler=Res_ISR)

#ISR of first interrupt (increment)
#we disable interrupt before its execution and the enable it after ISR ends for switch debouncing
def Inc_ISR(pin):
    Inc.irq(trigger=0, handler=Inc_ISR)
    global Global_Function1
    Global_Function1()
    Inc.irq(trigger=Pin.IRQ_FALLING, handler=Inc_ISR)

#ISR of second interrupt (decrement)
#we disable interrupt before its execution and the enable it after ISR ends for switch debouncing
def Dec_ISR(pin):
    Dec.irq(trigger=0, handler=Dec_ISR)
    global Global_Function2
    Global_Function2()
    Dec.irq(trigger=Pin.IRQ_FALLING, handler=Dec_ISR)

#ISR of third interrupt (reset)
#we disable interrupt before its execution and the enable it after ISR ends for switch debouncing
def Res_ISR(pin):
    Reset.irq(trigger=0, handler=Res_ISR)
    global Global_Function3
    Global_Function3()
    Reset.irq(trigger=Pin.IRQ_FALLING, handler=Res_ISR)