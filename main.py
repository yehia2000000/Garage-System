#Main script

#importing defined libraries
import LED
import SW
import SSD
import Sensor
import Wifi
import Server
import TIM
import INT

#timer ISR
def Timer_ISR(): #check for flag to perform suitable write operation
    global write_flag
    if(write_flag==1):
        Server.write_dec()
    elif(write_flag==2):
        Server.write_inc()

#initializing Timer    
TIM.Init(Timer_ISR)

#inc_ISR
def Inc_ISR():
    global Number
    print('done_inc')
    #loop while switch is still pressed
    while(SW.Inc.value()==0):
        pass
    #increment of number and sending it on seven segment and server
    Number+=1
    SSD.SendNumber(Number)
    Server.write_inc()

#dec_ISR
def Dec_ISR():
    global Number
    print('done_dec')
    #loop while switch is still pressed
    while(SW.Dec.value()==0):
        pass
    #decrement of number and sending it on seven segment and server
    Number-=1
    SSD.SendNumber(Number)
    Server.write_dec()

#reset_ISR
def Res_ISR():
    global Number
    print('done_res')
    #loop while switch is still pressed
    while(SW.Reset.value()==0):
        pass
    #reset of number and sending it on seven segment and server
    Number=0
    SSD.SendNumber(Number)
    Server.write_res()

Number=10 #initial value of number
Max_empty_locations=20 #max number of empty locations
write_flag=0 #flag to indicate write operation

#Establishing Wifi connection
Wifi.Connect()
LED.On2() #Activating led for indication

#sending number on seven segment
SSD.SendNumber(Number)

#Main loop
while 1:
    #indication if number of locations reached zero 
    if(Number==0):
        LED.On1()
    else:
        LED.Off1() 
    
    #checking mode of operation
    mode = SW.GetToggleValue()
    
    #Manual mode
    if mode==1:
        #initializing 3 interrupts
        INT.Init(Inc_ISR, Dec_ISR, Res_ISR)
        print('Manual')
        #establishing connection with server
        message = Server.listen()
        
        #taking action according to message recieved from server
        if(message.lower()=='inc'):
            Number+=1
        if(message.lower()=='dec'):
            Number-=1
        if(message.lower()=='res'):
            Number=0
        SSD.SendNumber(Number)
    
    #Automatic mode
    else:
        print('Automatic')
        #disabling interrupt
        INT.Disable()
        
        #establishing connection with server (no return value)
        Server.listen()
        #reading from IR sensor and detect in which direction car is moving
        direction = Sensor.Read()
        
        #case of car entering garage
        if(direction[0]==1):
            #entering
            print('entering')
            Number-=1
            SSD.SendNumber(Number)
            write_flag=1 #flag for indication in timer ISR
        #case of car leaving garage
        elif(direction[1]==1):
            #leaving
            print('leaving')
            Number+=1
            SSD.SendNumber(Number)
            write_flag=2 #flag for indication in timer ISR
        #no action detected by sensors
        else:
            write_flag=0