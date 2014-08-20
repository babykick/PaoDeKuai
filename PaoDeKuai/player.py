from game import *
from hand import Hand
from card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = None
        self.setup()
    
    def setup(self):
        pass

    def giveHand(self, hand):
        self.hand = hand

    def showHand(self):
        print self.hand
        
    def playTurn(self):
        raise NotImplementedError
        
    @property
    def Name(self):
        return self.name
    
    def getInput(self):
        cards = raw_input().split()
        pattern = self.hand.judgePattern(cards)
        if pattern:
            return pattern, [Card(c) for c in cards]
        return None
        

        
class HumanPlayer(Player):
    def playTurn(self):
        self.playCards(self.input)
    
    def setInput(self,input):
        self.input = input

    def __repr__(self):
        return "HumanPlayer('%s')" % self.Name

class ComputerPlayer(Player):  
    def setup(self):
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
    

