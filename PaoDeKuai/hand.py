import random

from .card import Card
from .combinations import (Bomb, SequenceOfPairTwo, SequenceOfSingle, SequenceOfTripletThree,
                           PairTwo, SingleCard, TripletThree)


class Deck(object):
    CARDFACE={0:"A", 1:"2", 2:"3", 3:"4", 4:"5", 5:"6",6:"7", 7:"8", 8:"9", 9:"10", 10:"J", 11:"Q", 12:"K"}
    #SUIT = {0:"Spade", 1:"Heart", 2:"Club", 3:"Diamond", 4:"black Joker", 5:"red Joker"}
    SUIT = {0:"S", 1:"H", 2:"C", 3:"D", 4:"bj", 5:"rj"}
    
    def __init__(self, exclude=None):
        """
          1-52 represent A-K with suits(spade, heart, club, diamond)
          53: black joker
          54: red joker
        """
        cards = [suit + point for point in Card.RANK.keys() for suit in Card.SUIT]
        cards.remove("sA")
        cards.remove("s2")
        cards.remove("h2")
        cards.remove("c2")
        self.cards = [Card(c) for c in cards]
        
 
    def remove_card(self, cardInd):
        self.cards.remove(cardInd)

    def shuffle(self):
        random.shuffle(self.cards)

    def dispatch(self, divideNum):
        if len(self.cards) % divideNum != 0:
           raise Exception("The card can not divided equally")

        each = len(self.cards)/divideNum
        result = []
        start = 0
        for i in range(divideNum):
           h = Hand()
           h.add_cards(self.cards[start:start + each])
           result.append(h)
           start += each

        return result
 
    def __repr__(self):
        return repr('<Deck %s>' % repr(self.cards))


class Hand(object):
    patterns = [Bomb, SequenceOfPairTwo, SequenceOfSingle, SequenceOfTripletThree,
                PairTwo, SingleCard, TripletThree]
    
    def __init__(self, cards=None):
        self.cards = cards or []
       
    def add_card(self, card):
        self.cards.append(card)
     
    def add_cards(self, cards):
        self.cards.extend(cards)

    def remove_cards(self, cards):
        for c in cards:
            self.cards.remove(c)
        
    def judge_pattern(self, cards):
        for cls in Hand.patterns:
            if cls.validate(cards):
                return cls(cards)
        else:
            return None
     
    def sort(self):
        self.cards.sort(key=lambda x: x.rank)

    def __repr__(self):
        self.sort()
        return '<Hand %s>' % repr(self.cards)
