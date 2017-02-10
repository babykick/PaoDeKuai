from .game import *
from .hand import Hand
from .card import Card

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = None
        self.setup()
    
    def setup(self):
        pass

    def play_cards(self):
        raise NotImplementedError

    def give_hand(self, hand):
        self.hand = hand

    def show_hand(self):
        print(self.hand)
        
    def play_turn(self):
        raise NotImplementedError

    
    def get_input(self):
        cards = [Card(c) for c in input().split()]
        pattern = self.hand.judgePattern(cards)
        return pattern
    
    def discard(self, cards):
        self.hand.removeCards(cards)
          
class HumanPlayer(Player):
    def play_turn(self):
        self.play_cards(self.input)
    
    def set_input(self,input):
        self.input = input

    def __repr__(self):
        return "<HumanPlayer('%s')>" % self.name

class ComputerPlayer(Player):  
    def setup(self):
        self.brain = RunFastAIEngine()
        
    def think(self):
        #self.brain.thinkAGoodPlay(curSituation)
        print('computer %s have a think...' % self.name)
         
    def play_turn(self):
        self.think()
        #self.playCards()
        print("computer %s play" % self.name)
        
    def __repr__(self):
        return "<ComputerPlayer('%s')>" % self.name
    

