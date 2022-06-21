import socket
import threading
import json
import pickle
from gameinfo import GameInfo
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
HEADER = 4096
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

def send_message_to_client(server, message):
    message = pickle.dumps(message)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    server.send(send_length)
    server.send(message)

def handle_client(connection, address, gameinfo):
    print(f"New connection {address} connected.".upper())
    gameinfo.setplayercount(gameinfo.playercount + 1)
    connected = True
    while connected:
        try:
            # checks if there is a message
            message_length = connection.recv(HEADER).decode(FORMAT)
            if message_length:
                message_length = int(message_length)
                player = pickle.loads(connection.recv(message_length))
                gameinfo.setplayerlist(player)
                send_message_to_client(connection, gameinfo.getplayerlist())

                print(f"{address}: sent their player")
        except Exception as e:
            print(e)
            connected = False

    connection.close()
    gameinfo.setplayercount(gameinfo.playercount - 1)


def start():
    # listens for connections
    gameinfo = GameInfo()
    server.listen()
    while 1:
        connection, adrress = server.accept()
        thread = threading.Thread(target=handle_client(connection, adrress, gameinfo))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")


print("The server is starting".upper())
start()
