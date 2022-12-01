import socket

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
    c.send("Thank you for connecting".encode())
    c.close()