#coding=utf-8

"""
 Poker game frame

"""

import random
from collections import Counter
from .player import *

from .hand import Deck



 
class Game(object):
    def __init__(self, deckset):
        self.players = []
        self.deckset = deckset
    
    def add_player(self, p):
        self.players.append(p)
        
         
    def start(self):
        who = random.randint(0, len(self.players)-1)
        while 1:
            print("player %s's turn: " % self.players[who].name)
            curPlayer = self.players[who]
            curPlayer.show_hand()
            while 1:
               print("what cards do you discard: ",)
               combination = curPlayer.get_input()
               if combination:
                  print(combination.name)
                  curPlayer.discard(combination.cards)
                  curPlayer.show_hand()
                  break
               else:
                  print("Input invalid")
            who = (who+1) % len(self.players)
   
    def setup(self):
        d = Deck()
        d.shuffle()
        hands = d.dispatch(3)
        self.players[0].giveHand(hands[0])
        self.players[1].giveHand(hands[1])
        self.players[2].giveHand(hands[2])
     
        
    
        
        
    
        
    
        
        
        
        




