import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Send data
    message = 'This is the message. It will be repeated'

    sock.sendall(message.encode('utf-8'))

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {}'.format(data))

finally:
    print('closing socket')
    sock.close()