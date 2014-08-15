from collections import Counter
from card import Card

class Combination:
    def __init__(self, cards=None):
        if isinstance(cards, basestring) or isinstance(cards, Card): # Single card case
            cards = [cards]
        if not self.validateFormat(cards):
            raise Exception("Format is not valid %s" % self.__class__.__name__)    
        if not self.validate(cards):
            raise Exception("Combination is not matched with %s" % self.__class__.__name__)
        self.cards = self.flatten(cards) 
   
   
    @classmethod
    def flatten(self, cards):
        """
           flatten the card objects list to simple card point list,
           leave only the card point
           example: given [card(s2), card(c3), card(h5)]
                    return [2, 3, 5]
          
        """
  
        return [Card.onlyPoint(card) for card in cards]
           
        
    
    @classmethod
    def validateFormat(cls, cards):
        """
          Check the format of cards representations
        """
        return all(Card.onlyPoint(c) for c in cards)
        
    
    @classmethod    
    def validate(self, cards):
        """
          Validate the combination, return True or False
        """
         
        
    def __cmp__(self, other):
        """
          Compare machanism
        """
    
    def __iter__(self):
        return iter(self.cards)
    
    
class SingleCard(Combination):
    @classmethod
    def validate(self, cards):
        return len(cards) == 1
    
    def __cmp__(self, other):
        return cmp(Card.getRank(self.cards[0]), Card.getRank(other.cards[0]))
    
    def __repr__(self):
        return str(self.__class__) + ": " + str(self.cards)



class PairTwo(Combination):
    @classmethod
    def validate(cls, cards):
        cs = cls.flatten(cards)
        return len(cs) == 2 and cs[0] == cs[1]
        
class TripletThree(Combination):
    """
       Triplet three or Triplet three with attach
    """
    @classmethod
    def validate(cls, cards):
        cs = cls.flatten(cards)
        # Todo

class Bomb(Combination):
    pass

        
class Sequence(Combination):
    pass


class SequenceOfSingle(Combinatjion):
    pass


class SequenceOfTripletThree(Sequence):
    pass

class SequenceOfPairTwo(Sequence):
    pass
        


