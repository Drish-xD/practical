import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")
host = socket.gethostname()
port = 1234
s.bind((host, port))
print("Socket binded to", host, ":",  port)
s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    currentTime = time.ctime(time.time())
    c.send(currentTime.encode())
    c.close()
