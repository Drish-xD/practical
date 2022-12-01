import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")
host = "127.0.0.1"
port = 1234
s.bind((host, port))
s.listen(5)
print("Welcome: The server is ready.")

while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    sentence = c.recv(2048).decode()
    print(">> ", sentence)
    message = input("Enter Message : ")
    c.send(message.encode())
    if (message == 'q'):
        c.close()
