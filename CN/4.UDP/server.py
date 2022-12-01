import socket

host = "127.0.0.1"
port = 1000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket successfully created")
s.bind((host, port))
print("Socket binded to", host, ":",  port)

while True:
    data, addr = s.recvfrom(1024)
    print("Got connection from", addr)
    print("Message >>> ", data)
