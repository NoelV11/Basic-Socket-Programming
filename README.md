# Basic-Socket-Programming

## About

This repository is dedicated to creation of sockets,which are essential in Ethical Hacking and Networking,for recieving reverse shells,connections and exploit development.

I have created a simple program,to recieve a reverse connection,via a specified port,using Netcat tool

## Functionality

The user/exploit developer specifies a port and IP Address,to recieve the reverse connection at.The 'socket' module availbale in Python is used for the same.

Variable 's' is instructed to take inputs - 'IP Address' (AF_INET) and 'Port' (SOCK_STREAM) and create a connection.

Here,we try to create a connection on the same machine,via port 4444

![S](https://user-images.githubusercontent.com/77625109/123251382-c4044180-d508-11eb-985c-7e90424d0513.jpg)

## Results

A short-loved connection is recieved

![Socket_Connection_Recieved](https://user-images.githubusercontent.com/77625109/123251783-36752180-d509-11eb-9b4d-3f2f55a0b47e.jpg)

Modifyng the same,using localhost (127.0.0.1)'s address,we get,

![Socket_Connection_Recieved(localhost)](https://user-images.githubusercontent.com/77625109/123251946-5dcbee80-d509-11eb-8cb4-f057868b4cd8.jpg)

## Result

This simple program helps us to recieve a reverse connection,which is essential,while running exploits/reverse shell code,to exploit a vulnerability/recieve a reverse connection
