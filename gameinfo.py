class GameInfo:
    def __init__(self):
        self.playerlist = []

    def setplayerlist(self, player):
        listindex = 0
        for i in self.playerlist:
            if i.name == player.name:
                self.playerlist[listindex] = player
                return 0
            listindex += 1
        print("added a player")
        self.playerlist.append(player)
    def getplayerlist(self):
        return self.playerlist
    def deleteaplayerinlist(self, playername):
        listindex = 0
        for i in self.playerlist:
            if i.name == playername:
                self.playerlist.pop(listindex)
                print("deleted a player")
            listindex += 1