import socket
import threading
import json
# loading the file
SERVERFILEREAD = open('server.json', 'r')
# loading the dictionary
SERVERFILE = json.load(SERVERFILEREAD)
SERVERFILEREAD.close()
# reading the variables for the server(its configurable this way)
PORT = SERVERFILE["PORT"]
SERVER = SERVERFILE["SERVER"]
# setting the hostname to the server.json file
SERVERFILE["HOSTNAME"] = socket.gethostname()
SERVERFILEWRITE = open("server.json", "w")
json.dump(SERVERFILE, SERVERFILEWRITE)
SERVERFILEWRITE.close()

# other variables
HEADER = 64
FORMAT = "utf-8"
DISCONNECTOR = "!DISCONNECT"

# prints the values of the hosted server
print(f"The port of the server = {PORT}".upper())
print(f"The servers ip = {SERVER}".upper())
print(f"The hostname = {socket.gethostname()}".upper())

# actual server setup
ADDRESS = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)


def handle_client(connection, address):
    print(f"New connection {address} connected.".upper())
    connected = True
    while connected:
        # checks if there is a message
        message_length = connection.recv(HEADER).decode(FORMAT)
        if message_length:
            message = connection.recv(int(message_length)).decode(FORMAT)
            print(f"{address} {message}")
            if message == DISCONNECTOR:
                connected = False
    connection.close()


def start():
    # listens for connections
    server.listen()
    while 1:
        connection, adrress = server.accept()
        thread = threading.Thread(target=handle_client(), args=(connection, adrress))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")


print("The server is starting".upper())
start()
