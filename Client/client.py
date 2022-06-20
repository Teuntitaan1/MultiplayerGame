import socket
HEADER = 64
PORT = 5050
FORMAT = "utf-8"
SERVER = "192.168.68.132"
ADDRESS = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def send(message):
    encodedmessage = message.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(encodedmessage)


while 1:
    send(input("Message: "))
