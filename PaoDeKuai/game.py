#coding=utf-8
########################
# Poker game frame
#
########################
import random
from collections import Counter
from .player import *
from .hand import Deck



 
class Game:
    def __init__(self, deckset):
        self.players = []
        self.deckset = deckset
    
    def addPlayer(self, p):
        self.players.append(p)
        
         
    def start(self):
        whosTurn = random.randint(0, len(self.players)-1)
        while 1:
            print "player %s's turn: " % self.players[whosTurn].name
            curPlayer = self.players[whosTurn]
            curPlayer.showHand()
            while 1:
               print "what cards do you discard: ",
               combination = curPlayer.getInput()
               if combination:
                  print combination.name
                  curPlayer.discard(combination.cards)
                  break
               else:
                  print "Input invalid"
            whosTurn = (whosTurn+1) % len(self.players)
   
    def setup(self):
        d = Deck()
        d.shuffle()
        hands = d.dispatch(3)
        self.players[0].giveHand(hands[0])
        self.players[1].giveHand(hands[1])
        self.players[2].giveHand(hands[2])
     
        
    
        
        
    
        
    
        
        
        
        




