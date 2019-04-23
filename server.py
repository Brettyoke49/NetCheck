import socket
import datetime

def stats_and_exit():
  end = datetime.datetime.now()
  total = end - start
  print("Finished after: ", total.total_seconds())

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9099        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print('Connected to: ', addr)
        start = datetime.datetime.now()
        while True:
          transmission = conn.recv(1024).decode()
          if(int(transmission) == -1):
            break;
          transmission = str(int(transmission) + 1)
          print("From client: ", transmission)
          conn.sendall(transmission.encode())

    stats_and_exit()

