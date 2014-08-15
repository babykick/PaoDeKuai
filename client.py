

class Client:
    def __init__(self, game):
        self.game = game
        game.setClient(self)
        
    def getInput(self):
        raise NotImplentedError
    
    def update(self):
        raise NotImplentedError

class GuiClient(Client):
    def getInput(self):
        pass

    def update(self):
        pass
    
    
class CommandLineClient(Client):    
    def getInput(self):
        return raw_input("cards to play: ")
    
    def update(self):
        print self.game.getPlayers()