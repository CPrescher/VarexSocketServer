import socket
import threading


def connect():
    sock = socket.socket()

    sock.connect(("localhost", 6060))
    print("Connected to localhost")

    msg = "blub"
    bytes = str.encode(msg)

    sock.sendall(bytes)
    sock.close()


print("Client - Main thread started")

threads = []
thread_num = 20

for ind in range(thread_num):
    thread = threading.Thread(target=connect())
    threads.append(thread)
    thread.start()

for ind in range(thread_num):
    threads[ind].join()
