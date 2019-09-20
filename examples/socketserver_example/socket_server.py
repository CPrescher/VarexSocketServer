import socketserver
import threading

server_address = ("localhost", 6060)


class MyTCPClientHandler(socketserver.StreamRequestHandler):
    def handle(self):
        # Receive and print the data received from client
        print('Received one request from {}'.format(self.client_address[0]))
        msg = self.rfile.readline().strip()
        print("Data received from client is:")
        print(msg)
        print("Thread Name: {}".format(threading.current_thread().name))


# Create a Server Instance
tcp_socket_server = socketserver.ThreadingTCPServer(server_address, MyTCPClientHandler)

# Make the server wait forever serving connections
tcp_socket_server.serve_forever()
