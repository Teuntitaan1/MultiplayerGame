import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.68.132"
        self.port = 5050
        self.address = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except Exception as e:
            print(e)

    def send(self, data):

        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048 * 8))
        except socket.error as e:
            print(e)

