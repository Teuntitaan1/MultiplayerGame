import pickle
import socket
from _thread import *

from gameinfo import GameInfo

# server variables
PORT = int(input("What port should the server run on?"))
SERVER = socket.gethostbyname(socket.gethostname())
SERVERNAME = socket.gethostname()


# prints the values of the hosted server
print(f"The port of the server = {PORT}".upper())
print(f"The servers ip = {SERVER}".upper())
print(f"The hostname = {SERVERNAME}".upper())

# actual server setup
ADDRESS = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind(ADDRESS)
except socket.error as e:
    print(e)
server.listen()
print("Server has started".upper())


def handle_client(connection, address):
    print(f"New player {address} connected.".upper())
    connection.send(str.encode("Connected"))

    connected = True
    oldpacket = None
    while connected:
        try:

            newpacket = pickle.loads(connection.recv(2048))
            if newpacket != oldpacket:
                oldpacket = newpacket


            gameInfo.setplayerlist(newpacket)
            reply = gameInfo.getplayerlist()
            connection.send(pickle.dumps(reply))
        except Exception as error:
            print(error)
            gameInfo.deleteaplayerinlist(oldpacket.name)
            connected = False
    print(f"{address} has disconnected")
    connection.close()

def handlenemies(gameInfo, enemies):
    while 1:
        pass

gameInfo = GameInfo()
print("Entered the loop".upper())
enemies = "lol"
# start_new_thread(handlenemies, (gameInfo, enemies))
# server loop
while 1:
    connection, adrress = server.accept()
    start_new_thread(handle_client, (connection, adrress))
