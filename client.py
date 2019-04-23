import socket
import signal
import sys

def signal_handler(sig, frame):
        sock.sendall(str(-1).encode())
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9099        # The port used by the server


transmission = str(0);

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
      sock.sendall(transmission.encode())
      transmission = sock.recv(1024).decode()
      transmission = str(int(transmission) + 1)
      print("From server: ", transmission)

print('Received', repr(data))
