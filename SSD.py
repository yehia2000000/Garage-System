#Library for seven segment display

#importing module for GPIO initialization
from machine import Pin

#first BCD to seven segmet converter connections
In1_pinA = 15
In2_pinA = 18
In4_pinA = 5
In8_pinA = 4

#second BCD to seven segmet converter connections
In1_pinB = 19
In2_pinB = 23
In4_pinB = 22
In8_pinB = 21

#Common pin of second seven segment(Tens display)
En_pin = 14

#initializing all previous pins as output
IN1_A = Pin(In1_pinA, Pin.OUT, value=0)
IN2_A = Pin(In2_pinA, Pin.OUT, value=0)
IN4_A = Pin(In4_pinA, Pin.OUT, value=0)
IN8_A = Pin(In8_pinA, Pin.OUT, value=0)
IN1_B = Pin(In1_pinB, Pin.OUT, value=0)
IN2_B = Pin(In2_pinB, Pin.OUT, value=0)
IN4_B = Pin(In4_pinB, Pin.OUT, value=0)
IN8_B = Pin(In8_pinB, Pin.OUT, value=0)
EN = Pin(En_pin, Pin.OUT, value=1) #to be initialy disabled

#function to enable second seven segment
def Enable():
    EN.off()

#function to disable second seven segment
def Disable():
    EN.on()

#function to send number to first seven segment
def SendNumberUnits(Num):
    if Num==0:
        IN1_A.off()
        IN2_A.off()
        IN4_A.off()
        IN8_A.off()
    if Num==1:
        IN1_A.on()
        IN2_A.off()
        IN4_A.off()
        IN8_A.off()
    if Num==2:
        IN1_A.off()
        IN2_A.on()
        IN4_A.off()
        IN8_A.off()
    if Num==3:
        IN1_A.on()
        IN2_A.on()
        IN4_A.off()
        IN8_A.off()
    if Num==4:
        IN1_A.off()
        IN2_A.off()
        IN4_A.on()
        IN8_A.off()
    if Num==5:
        IN1_A.on()
        IN2_A.off()
        IN4_A.on()
        IN8_A.off()
    if Num==6:
        IN1_A.off()
        IN2_A.on()
        IN4_A.on()
        IN8_A.off()
    if Num==7:
        IN1_A.on()
        IN2_A.on()
        IN4_A.on()
        IN8_A.off()
    if Num==8:
        IN1_A.off()
        IN2_A.off()
        IN4_A.off()
        IN8_A.on()
    if Num==9:
        IN1_A.on()
        IN2_A.off()
        IN4_A.off()
        IN8_A.on()

#function to send number to second seven segment
def SendNumberTens(Num):
    if Num==0:
        IN1_B.off()
        IN2_B.off()
        IN4_B.off()
        IN8_B.off()
    if Num==1:
        IN1_B.on()
        IN2_B.off()
        IN4_B.off()
        IN8_B.off()
    if Num==2:
        IN1_B.off()
        IN2_B.on()
        IN4_B.off()
        IN8_B.off()
    if Num==3:
        IN1_B.on()
        IN2_B.on()
        IN4_B.off()
        IN8_B.off()
    if Num==4:
        IN1_B.off()
        IN2_B.off()
        IN4_B.on()
        IN8_B.off()
    if Num==5:
        IN1_B.on()
        IN2_B.off()
        IN4_B.on()
        IN8_B.off()
    if Num==6:
        IN1_B.off()
        IN2_B.on()
        IN4_B.on()
        IN8_B.off()
    if Num==7:
        IN1_B.on()
        IN2_B.on()
        IN4_B.on()
        IN8_B.off()
    if Num==8:
        IN1_B.off()
        IN2_B.off()
        IN4_B.off()
        IN8_B.on()
    if Num==9:
        IN1_B.on()
        IN2_B.off()
        IN4_B.off()
        IN8_B.on()

#function that displays any number on the seven segment display(smaller or greater than 9)
def SendNumber(Num):
    #case of one digit number
    if Num<10:
        Disable()
        SendNumberUnits(Num)
    #case of two-digit number
    else:
        digits = [int(x) for x in str(Num)] #seperating number in to a list of its digits
        SendNumberUnits(digits[1])
        SendNumberTens(digits[0])
        Enable()
