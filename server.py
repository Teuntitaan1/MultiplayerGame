import socket
from _thread import *
import json
import pickle
from gameinfo import GameInfo
from player import Player
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
FORMAT = "utf-8"
DISCONNECTOR = "!DISCONNECT"

# prints the values of the hosted server
print(f"The port of the server = {PORT}".upper())
print(f"The servers ip = {SERVER}".upper())
print(f"The hostname = {socket.gethostname()}".upper())

# actual server setup
ADDRESS = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("The server is starting".upper())
try:
    server.bind(ADDRESS)
except socket.error as e:
    print(e)
print("Server has started".upper())
server.listen(2)


def handle_client(connection, address):
    print(f"New connection {address} connected.".upper())
    connection.send(str.encode("Connected"))

    connected = True
    while connected:
        try:
            data = pickle.loads(connection.recv(2048))
            gameInfo.setplayerlist(data)
            reply = gameInfo.getplayerlist()
            print("Recieved: ", reply)
            print("Send:", reply)
            connection.sendall(pickle.dumps(reply))
        except Exception as e:
            print(e)
            gameInfo.deleteaplayerinlist(data)
            connected = False
    print(f"{address} has disconnected")
    connection.close()

gameInfo = GameInfo()
print("Entered the loop".upper())
# server loop
while 1:
    connection, adrress = server.accept()
    start_new_thread(handle_client, (connection, adrress))




