class GameInfo:
    def __init__(self):
        self.playercount = 0
        self.playerlist = []

    def setplayercount(self, count):
        self.playercount = count

    def setplayerlist(self, player):
        set = False
        for i in self.playerlist:
            if i["playername"] == player["playername"]:
                i["x"] = player["x"]
                i["y"] = player["y"]
                set = True
        if not set:
            print("added a player")
            self.playerlist.append(player)

        self.playerlist.append(player)
    def getplayercount(self):
        return self.playercount
    def getplayerlist(self):
        return self.playerlist