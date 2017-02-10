

class Client(object):
    def __init__(self, game):
        self.game = game
        game.setClient(self)
        
    def getInput(self):
        raise NotImplementedError
    
    def update(self):
        raise NotImplementedError


class GuiClient(Client):
    def getInput(self):
        pass

    def update(self):
        pass
    
    
class CommandLineClient(Client):    
    def getInput(self):
        return input("cards to play: ")
    
    def update(self):
        print(self.game.getPlayers())