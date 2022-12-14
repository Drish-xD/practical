import socket

port = 1000
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(5)

print('Server listening....')

while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename = 'mytext.txt'

    f = open(filename, 'rb')
    l = f.read(1024)

    while (l):
        conn.send(l)
        print('Sending', repr(l))
        f.close()
        print('Successfully Sent')

    conn.send('Thank you for connecting')
    conn.close()
