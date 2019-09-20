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

num_images = 0

times = []

while True:
    # Wait for connection

    t1 = time.time()
    print('Waiting for a connection')
    connection, client_address = sock.accept()
    print('connection from', client_address)

    try:
        buffer_size = 2880 * 2880 * 16
        byte_data = connection.recv(buffer_size)
        data = np.load(io.BytesIO(byte_data))
        num_images += 1
    except ValueError:
        pass

    finally:
        connection.close()
        times.append(time.time()-t1)
        print('{} images received'.format(num_images))
        print('{} Hz Transmission rate'.format(1/np.mean(times[-10:])))
