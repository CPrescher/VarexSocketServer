import socket
import time

import numpy as np

server_address = ('localhost', 10000)


def connect_and_send():
    sock = socket.socket()
    sock.connect(server_address)
    print("Connected to localhost")
    data = np.ones((2880, 2880), dtype='uint16')
    sock.sendall(data.tobytes())
    sock.close()


for i in range(50):
    t1 = time.time()
    connect_and_send()
    processing_time = time.time() - t1
    try:
        time.sleep(0.1 - processing_time)
    except ValueError:
        pass
