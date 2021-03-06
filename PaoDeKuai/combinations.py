from collections import Counter

from.utils import compare
from .card import Card



class Combination(object):
    def __init__(self, cards=None):
        if isinstance(cards, str) or isinstance(cards, Card): # Single card case
            cards = [cards]
        if not self.validate_format(cards):
            raise Exception("Format is not valid %s" % self.__class__.__name__)    
        if not self.validate(cards):
            raise Exception("Combination is not matched with %s" % self.__class__.__name__)
        self.cards = cards   # Original 
        self.fcards = self.flatten(cards) # Flattened 
   
   
    @classmethod
    def flatten(cls, cards):
        """
           flatten the card objects list to simple card point list,
           leave only the card point
           example: given [card(s2), card(c3), card(h5)]
                    return [2, 3, 5]
          
        """
  
        return [Card.onlyPoint(card) for card in cards]
           
    @classmethod
    def count(cls, cards):
        return dict(Counter(cls.flatten(cards)))
    
    @classmethod
    def validate_format(cls, cards):
        """
          Check the format of cards representations
        """
        return all(Card.onlyPoint(c) for c in cards)
        
    
    @classmethod    
    def validate(cls, cards):
        """
          Validate the combination, return True or False
        """
    
    @property
    def name(self):
        return self.__class__.__name__
        
        
    def __cmp__(self, other):
        """
          Compare machanism
        """
    
    def __iter__(self):
        return iter(self.fcards)
    
    
    def __len__(self):
        return len(self.cards)


class SingleCard(Combination):
    @classmethod
    def validate(cls, cards):
        return len(cards) == 1
    
    def __cmp__(self, other):
        return compare(self.cards[0].rank, other.cards[0].rank)
    
    def __repr__(self):
        return str(self.__class__) + ": " + str(self.fcards)

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        pass


class PairTwo(Combination):
    @classmethod
    def validate(cls, cards):
        cs = cls.flatten(cards)
        return len(cs) == 2 and cs[0] == cs[1]

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        pass
        
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
        if len(self.fcards) == 3: return "no"
        cnt = self.count(self.fcards).values()
        if cnt.count(2) == 1: return "pair"
        if cnt.count(1) == 1: return "single"
        if cnt.count(1) == 2: return "two-single"

class Bomb(Combination):
    @classmethod
    def validate(cls, cards):
        cards = cls.flatten(cards)
        return len(cards) == 4 and cls.count(cards).values().count(4) == 1
        
    def attachment(self):
        if len(self.fcards) == 4: return "no"
        cnt = self.count(self.fcards).values()
        if cnt.count(2) == 1: return "pair"
        if cnt.count(1) == 1: return "single"
        if cnt.count(1) == 2: return "two-single"
        
    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        pass

        
class Sequence(Combination):
    @classmethod
    def extract(cls, cards):
        """
          This method extracts the elements of same occurence by counting the elements.
          The occurence is the max occurence count.
        """
        cs = cls.flatten(cards)
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
       return len(self.extract(self.fcards)[0])
    
    # def __cmp__(self, other):
    #     assert len(self) == len(other)
    #     seq1, _ = self.extract(self.cards)
    #     seq2, _ = self.extract(other.cards)
    #     return compare(seq1[0], seq2[0])

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        pass
    
class SequenceOfSingle(Sequence):
    @classmethod
    def validate(cls, cards):
        return len(cards) >= 5 and cls.isSeq(cards)
 
    # def __cmp__(self, other):
    #     assert len(self) == len(other)
    #     return compare(sorted(self.fcards)[0], sorted(other.cards)[0])

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        pass

     
class SequenceOfTripletThree(Sequence):
    @classmethod
    def validate(cls, cards):
        seq, repeat = cls.extract(cards)
        cnt = cls.count(cards).values()
        attachnum = cnt.count(1) + cnt.count(2) * 2 
        return (repeat == 3 and cls.isSeq(seq)) and \
               ((attachnum == len(seq) * 2) or \
                (attachnum == len(seq)) or \
                 attachnum == 0)
                
     
class SequenceOfPairTwo(Sequence):
    @classmethod
    def validate(cls, cards):
        seq, repeat = cls.extract(cards)
        return cls.isSeq(seq) and repeat==2 and len(cards) == len(seq) * 2
    #
    # def __cmp__(self, other):
    #     return compare(self.fcards[0], other.cards[0])
    #
    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        pass


