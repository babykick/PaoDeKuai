from game import *
from Engine import *

class Player:
    def __init__(self, name):
        self.name = name

    def playCards(self, cardsStr):
        self.hand.play(cardsStr)

    def addHand(self, hand):
        self.hand = hand
        
    def getHand(self):
        return self.hand

    def showHand(self):
        print self.hand.toString()
        
    def playTurn(self):
        raise NotImplementedError
        
    @property
    def Name(self):
        return self.name

        
class HumanPlayer(Player):
    def playTurn(self):
        self.playCards(self.input)
    
    def setInput(self,input):
        self.input = input

    def __repr__(self):
        return "HumanPlayer('%s')" % self.Name

class ComputerPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.brain = RunFastAIEngine()
        
        
    def think(self):
        #self.brain.thinkAGoodPlay(curSituation)
        print 'computer %s have a think...' % self.name
         
    def playTurn(self):
        self.think()
        #self.playCards()
        print "computer %s play" % self.name
        
    def __repr__(self):
        return "ComputerPlayer('%s')" % self.Name
    

