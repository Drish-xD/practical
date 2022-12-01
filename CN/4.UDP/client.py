import socket

host = "127.0.0.1"
port = 1000
message = ("Hello World!!!").encode()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(message, (host, port))
print("Successfully sent message")
