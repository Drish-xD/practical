import socket
import threading

host = socket.gethostname()
port = 1234


def client_thread(conn, addr):
    with conn:
        print("Connected to ", addr)

        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(("Received ", data,  " from ", addr).encode())

    print("Disconnected from", addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")
s.bind((host, port))
s.listen(5)
print("Welcome: The server is ready.")

while True:
    c, addr = s.accept()
    print("Starting thread for connection")
    thread = threading.Thread(target=client_thread, args=(conn, addr))
    thread.start()
