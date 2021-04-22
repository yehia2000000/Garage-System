#library for getting reading from sensors

#importing module for GPIO and ADC initialization
from machine import Pin,ADC

#threshold value for IR detection
Threshold = 3910

#Pins of 2 sensors
IR_sensor1 = 32
IR_sensor2 = 33

#initializing adc channels
Sensor1 = ADC(Pin(IR_sensor1))
Sensor2 = ADC(Pin(IR_sensor2))

#increasing voltage range to be (0-3.6v)
Sensor1.atten(ADC.ATTN_11DB)
Sensor2.atten(ADC.ATTN_11DB)

#function to read 2 sensors and return 1 if an object is detected in front of any sesnor
def Read():
    #initalizing a list of 2 values to be returned as readings of sensors
    Readings = [0,0]
    #Readings[0] -> First Sensor
    #Readings[0] -> Second sensor
    
    #reading first sensor
    if Sensor1.read()>Threshold:
        Readings[0]=1
    else:
        Readings[0]=0
        
    #reading second sensor
    if Sensor2.read()>Threshold:
        Readings[1]=1
    else:
        Readings[1]=0
    
    #returning the list containing the readings of both sensors
    return Readings