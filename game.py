#coding=utf-8
########################
# Poker game frame
#
########################
import random
from collections import Counter
from player import *


class Board:
    def __init__(self):
        self.playedCards = Counter()
        
    def placeCard(self, card):
        self.playedCards[card.CardFace] += 1
        
    def placePattern(self, pattern):
        for c in pattern:
            self.placeCard(c)

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []
        
    def setClient(self, client):
        self.client = client 
        
    def start(self):
        whosTurn = random.randint(0, len(self.players)-1)
        while 1:
            curPlayer = self.players[whosTurn]
            if isinstance(curPlayer, HumanPlayer):
                curPlayer.showHand()
                curPlayer.setInput(self.client.getInput().strip())
            curPlayer.playTurn()
            self.client.update()
            whosTurn += 1
            whosTurn = whosTurn % len(self.players)
        
    def addPlayer(self, name, playerType):
        if playerType == "human":
            self.players.append(HumanPlayer(name))
        elif playerType == "computer":
            self.players.append(ComputerPlayer(name))
         
    def getPlayers(self):
        return self.players
    
    
    def dispatch(self):
        deck = Deck(exclude=[1,15,28,41,53,54]) # throw one "A" and three "2"
        deck.shuffle()
        hands = deck.dispatchHands(len(self.players))
        for player in self.players: 
           hand = hands.pop()
           hand.sort()
           player.addHand(hand) 
           
        
           
           
        
    
        
        
    
        
    
        
        
        
        




