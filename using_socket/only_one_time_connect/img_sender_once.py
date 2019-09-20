import socket
import io
import time

import numpy as np

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))

sock.connect(server_address)

for i in range(50):
    # Send data in 10 hz
    t1 = time.time()

    data = np.ones((2880, 2880), dtype='uint16')
    bytestream = io.BytesIO()
    np.save(bytestream, data)

    sock.sendall(bytestream.getvalue())
    processing_time = time.time() - t1
    print('Send image in {} s'.format(processing_time))
    time.sleep(0.1 - processing_time)

sock.close()
