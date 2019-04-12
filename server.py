import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9099        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print('Connected to: ', addr)
        while True:
          data = conn.recv(1024).decode()
          data = str(int(data) + 1)
          print("From client: ", data)
          if not data: break
          conn.sendall(data.encode())
