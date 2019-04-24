import socket
import signal
import sys
import datetime

def signal_handler(sig, frame):
        sock.sendall(str(-1).encode())
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

HOST = '127.0.0.1'  # The server's default IP address
PORT = 9099        # The default port used by the server
NormDuration = 60 # Default time for normal measurements
DosDuration = 60 # Default time for DoS measurements

if(len(sys.argv) >= 2 and str(sys.argv[1]) == "-h") : # Help option
  print("Usage: python3 client.py [Normal_Duration] [DoS_Duration] [HOST] [PORT]")
  print("Set Durations in seconds, default is 60 seconds each")
  print("Default HOST is localhost (127.0.0.1), default PORT is 9099")
  print("Durations must be set together or not at all, same with HOST/PORT")
  exit()

if(len(sys.argv) >= 3) : # Capturing arguments
  NormDuration = int(sys.argv[1])
  DosDuration = int(sys.argv[2])
  if(len(sys.argv) >= 5) :
    HOST = sys.argv[3]
    PORT = int(sys.argv[4])

feedbackInterval = NormDuration / 10
transmission = str(0);
intervals = 1;
DoSing = False;

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, int(PORT)))
    print("If you must end the program early, use Ctrl-C on the CLIENT (this) program. NOT the server!")
    start = datetime.datetime.now()

    while True: # Main transmission loop
      sock.sendall(transmission.encode()) # Send/Receive
      transmission = sock.recv(1024).decode()
      transmission = str(int(transmission) + 1)

      if(int(transmission) % 10 == 0) : # Check for necessary updates
        timeElapsed = datetime.datetime.now() - start
        if(timeElapsed.total_seconds() > feedbackInterval) :
          if(intervals == 10) : # Handle transition to DoS phase and end of program in this block
            if(DoSing) : # End of program
              print("\nTerminating Session...")
              signal_handler(signal.SIGINT, 0)
            else :
              print("\nTransitioning to DoS phase for", DosDuration, "seconds.") # Start DoS
              feedbackInterval = DosDuration / 10
              DoSing = True;
              intervals = 1
              transmission = str(0)
              start = datetime.datetime.now()
          else :
            print(intervals * 10, "%... ", end = "", sep = '')
            sys.stdout.flush()
            intervals += 1
            start = datetime.datetime.now()


print('Received', repr(data))
