import socket
import datetime
import sys
import subprocess

def stats_and_exit():
  end = datetime.datetime.now()
  total = end - start
  print("Finished after: ", total.total_seconds())
  print("Number of router hops between server and client: ", length)
  print("Total normal transmissions: ", switchTrans)
  print("Total distressed transmissions: ", prevTransmission)


  halfOne = switchTime - start
  halfTwo = end - switchTime
  normTPS = int(switchTrans) / halfOne.total_seconds()
  dosTPS = int(prevTransmission) / halfTwo.total_seconds()

  print("\nNormal transmissions per second: ", int(normTPS))
  print("Distressed transmissions per second: ", int(dosTPS))



HOST = '127.0.0.1'  # Default IP to connect to
PORT = 9099        # Default Port to listen on

if(len(sys.argv) >= 2 and str(sys.argv[1]) == "-h") :
  print("Usage: python3 server.py [HOST] [PORT]\nDefault HOST is localhost, default PORT is 9099")
  exit()

if(len(sys.argv) >= 2) :
  HOST = sys.argv[1]
  if(len(sys.argv) >= 3) :
    PORT = sys.argv[2]

prevTransmission = -1;

subCmd = "traceroute " + HOST + " | wc -l"
routeInfo = subprocess.run(['traceroute', HOST], stdout=subprocess.PIPE) # Get initial traceroute so future calls are quicker
length = len((routeInfo.stdout.decode('utf-8')).split('\n')) - 2

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, int(PORT)))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print('Connected to: ', addr)
        print("If you must end the program early, use Ctrl-C on the CLIENT program. NOT the server (this)!")


        start = datetime.datetime.now()

        while True:
          transmission = conn.recv(1024).decode()

          if(int(transmission) == 0) : # When the client switches to DoS mode
            switchTime = datetime.datetime.now()
            switchTrans = prevTransmission
          else :
            try:
              if(int(transmission) != int(prevTransmission) + 1 and int(transmission) != 0) :
                break;
            except:
              break;

          transmission = str(int(transmission) + 1)
          prevTransmission = transmission
          conn.sendall(transmission.encode())

    stats_and_exit()
