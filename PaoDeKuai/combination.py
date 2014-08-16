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
    def count(self, cards):
        return dict(Counter(self.flatten(cards)))    
    
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
        values = cls.count(cards).values()
        
        return (len(cards) == 3 and values.count(3) == 1) or \
               (len(cards) == 4 and values.count(3) == 1 and values.count(1)==1) or \
               (len(cards) == 5 and values.count(3) ==1 and (values.count(1)==2 or values.count(2)==1))
   
    def attachment(self):
        if len(self.cards) == 3: return "no"
        cnt = self.count(self.cards).values()
        if cnt.count(2) == 1: return "pair"
        if cnt.count(1) == 1: return "single"
        if cnt.count(1) == 2: return "two-single"

class Bomb(Combination):
    @classmethod
    def validate(cls, cards):
        cards = cls.flatten(cards)
        return len(cards) == 4 and cls.count(cards).values().count(4) == 1
        
    def attachment(self):
        if len(self.cards) == 4: return "no"
        cnt = self.count(self.cards).values()
        if cnt.count(2) == 1: return "pair"
        if cnt.count(1) == 1: return "single"
        if cnt.count(1) == 2: return "two-single"
        
    
        
class Sequence(Combination):
    @classmethod
    def extract(self, cards):
        """
          This method extracts the elements of same occurence by counting the elements.
          The occurence is the max occurence count.
        """
        cs = self.flatten(cards)
        cnt = Counter(cs)
        maxCount = cnt.most_common()[0][1]
        return ([elem for elem in cnt.keys() if cnt.get(elem) == maxCount], maxCount)
                
    
    @classmethod
    def isSeq(cls, cards):
        """
          Check if the seq are incredent and step by one
        """
        cards = cls.flatten(cards)
        if not all(Card.canInSeq(c) for c in cards):return False
        if len(cards) < 2: return False
        ranks = sorted(Card.getRank(c) for c in cards)
        return all(ranks[i] + 1 == ranks[i+1] for i in range(len(ranks)-1))
     
    def __len__(self):
        return len(self.extract(self.cards)[0])
    
class SequenceOfSingle(Sequence):
    @classmethod
    def validate(cls, cards):
        return len(cards) >= 5 and cls.isSeq(cards)
 
    def __cmp__(self, other):
        if len(self) != len(other):
            raise Exception("The sequence should be equal to compare") 
                           
        return cmp(sorted(self.cards)[0], sorted(other.cards)[0])

class SequenceOfTripletThree(Sequence):
    @classmethod
    def validate(cls, cards):
        seq, repeat = cls.extract(cards)
        print seq
        cnt = cls.count(cards).values()
        attachnum = cnt.count(1) + cnt.count(2) * 2 
        return (repeat == 3 and cls.isSeq(seq)) and \
               ((attachnum == len(seq) * 2) or \
                (attachnum == len(seq)) or \
                 attachnum == 0)
                
     
class SequenceOfPairTwo(Sequence):
    pass
        


