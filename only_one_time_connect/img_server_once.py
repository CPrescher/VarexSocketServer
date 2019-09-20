import socket
import io
import time

import numpy as np

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
sock.bind(server_address)
print('Starting up on {} port {}'.format(*server_address))

# Listen for incoming connections
sock.listen()

while True:
    # Wait for connection
    print('Waiting for a connection')
    connection, client_address = sock.accept()
    print('connection from', client_address)

    num_images = 0
    t1 = time.time()

    try:
        while True:
            buffer_size = 2880 * 2880 * 16
            byte_data = connection.recv(buffer_size)
            data = np.load(io.BytesIO(byte_data))
            num_images += 1
            print('Time: {}  Average: {}'.format(time.time(), np.mean(data)))
    except ValueError:
        pass
    finally:
        connection.close()
        print('{} images received'.format(num_images))
        print('{} Hz Transmission rate'.format((num_images - 1) / (time.time() - t1)))
