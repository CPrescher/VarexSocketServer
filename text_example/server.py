import socket

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
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received {}'.format(data))

            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no more data from {}'.format(client_address))
                break
    finally:
        connection.close()


