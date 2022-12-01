import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1234
s.connect((host, port))
s.send('Hello world!'.encode())
time.sleep(4)
s.shutdown(1)
s.close()
