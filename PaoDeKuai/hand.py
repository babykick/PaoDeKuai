from card import Card
import random
from combination import Bomb, SequenceOfPairTwo, SequenceOfSingle, SequenceOfTripletThree, PairTwo, SingleCard, TripletThree


class Deck:
    CARDFACE={0:"A", 1:"2", 2:"3", 3:"4", 4:"5", 5:"6",6:"7", 7:"8", 8:"9", 9:"10", 10:"J", 11:"Q", 12:"K"}
    #SUIT = {0:"Spade", 1:"Heart", 2:"Club", 3:"Diamond", 4:"black Joker", 5:"red Joker"}
    SUIT = {0:"S", 1:"H", 2:"C", 3:"D", 4:"bj", 5:"rj"}
    
    def __init__(self, exclude=[]):
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
        
 
    def removeCard(self, cardInd):
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
           h.addCards(self.cards[start:start + each])
           result.append(h)
           start += each

        return result
 
    def __repr__(self):
      
        return repr(self.cards)

class Hand:
    patterns = [Bomb, SequenceOfPairTwo, SequenceOfSingle, SequenceOfTripletThree, PairTwo, SingleCard, TripletThree]
    
    def __init__(self, cards=None):
        self.cards = cards or []
       
    def addCard(self, card):
        self.cards.append(card)

    def addCards(self, cards):
        self.cards.extend(cards)

    def judgePattern(self, cards):
        for p in self.patterns:
            if p.validate(cards):
                return p
        else:
            return None
     
    def sort(self):
        self.cards.sort(key=lambda x: x.rank)

    def __repr__(self):
        self.sort()
        return repr(self.cards)
