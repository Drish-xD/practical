import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 1234
s.connect((host, port))

while True:
    message = input("Enter Message : ")
    s.send(message.encode())
    sentence = s.recv(2048).decode()
    print(">> ", sentence)
    if (message == 'q'):
        s.close()
