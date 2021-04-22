#Library to communicate with server

#importing module that provides access to server
import usocket

#initializing socket (TCP connection)
sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
sock.bind(('192.168.4.1',80)) #ip address of esp32 & port=80
sock.listen(2) #enabling a server to accept connections

#flags that indicate which operation we need to perform in the server
inc_flag=0
dec_flag=0
res_flag=0
#flag that indicate wether we are in the first iteration or not
first=0

#function to send increment indication to application
def write_inc():
    global inc_flag
    inc_flag=1
    
#function to send decrement indication to application
def write_dec():
    global dec_flag
    dec_flag=1
    
#function to send reset indication to application
def write_res():
    global res_flag
    res_flag=1

#main function for server
def listen():
    #making the variables in the global scope
    global inc_flag
    global dec_flag
    global res_flag
    global first
    global text
    global conn
    #check if any of the flag is raised in the beggining of the function
    if((inc_flag==0) and (dec_flag==0) and (res_flag==0)):
        if (first==1): #close connection if only we passed the first iteration
            conn.close()
        print('Waiting for request')
        conn, addr = sock.accept() #accept a connection for socket
        req = conn.recv(1024) #receiving data from the socket
        text = str(req) #converting data to string
    #sending data to server
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text\html\n')
    conn.send('\n')
    #checking for raised flag in order to perform the suitable operation
    if(inc_flag==1):
        inc_flag=0
        print('inc_flag')
        conn.sendall('Increment\n')
    elif(dec_flag==1):
        dec_flag=0
        print('dec_flag')
        conn.sendall('Decrement\n')
    elif(res_flag==1):
        res_flag=0
        print('res_flag')
        conn.sendall('Reset\n')
    else:
        conn.sendall('Request Recieved\n')
    
    #indicating that we passed the first iteration
    first=1
    
    return text[7:10] #returning 3 letter message (inc or dec or reset)