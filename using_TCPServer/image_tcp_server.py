import socketserver
import time

import numpy as np

server_address = ('localhost', 10000)

RES = 2880  # This value is for both X and Y axes
IMG_BYTES_COUNT = 2 * (RES ** 2)  # uint16 for the image matrix


class MyTCPClientHandler(socketserver.StreamRequestHandler):
    num_images = 0
    times = []
    t1 = time.time()

    def handle(self):
        # Receive and print the data received from client
        data = self.rfile.read(IMG_BYTES_COUNT)
        data_bytes = bytearray()
        data_bytes.extend(data)
        img_data = np.frombuffer(data_bytes, dtype=np.uint16).reshape(RES, RES)

        self.num_images += 1
        self.times.append(time.time()-self.t1)
        print('Time: {}  Average: {}'.format(time.time(), np.mean(img_data)))
        print('{} Hz Transmission rate'.format(1/np.mean(np.diff(self.times[-8:]))))


# Create a Server Instance
tcp_socket_server = socketserver.ThreadingTCPServer(server_address, MyTCPClientHandler)

# Make the server wait forever serving connections
tcp_socket_server.serve_forever(poll_interval=3)
