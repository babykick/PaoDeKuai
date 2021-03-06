


class Card(object):
    RANK = {'3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, 'T':8,
            "J":9, "Q":10, "K":11, "A":12, "2":13}
    SUIT = ["s", "c", "h", "d"]
    JOKERS = ["bj", "rj"]
    
    def __init__(self, cardName=None, suit=None, point=None):
        s, p = None, None
        if cardName and not point and not suit:    
           s, p  = cardName[0], cardName[1]
        elif not cardName and point and suit:
           s, p = suit, point
        if not self.validate(suit=s, point=p):
            raise Exception("Card name is not valid")
        self._suit = s
        self._point = p
        
        
    @classmethod
    def validate(cls, suit, point):
        return (point in Card.RANK.keys()) and (suit in Card.SUIT)
        
    @property    
    def point(self):
        return self._point
    
    @property
    def rank(self):
        return self.getRank(self.point)
     
    @classmethod 
    def getRank(cls, card):
        return Card.RANK.get(cls.onlyPoint(card))
     
    @property
    def suit(self):
        return self._suit
    
    @classmethod
    def setComparor(cls, comp):
        cls.comparor = comp
        
    @classmethod
    def canInSeq(cls, card):
        point = cls.onlyPoint(card)
        return not point in ("2",)
    
    @classmethod
    def onlyPoint(cls, card):
         if isinstance(card, str):
            if len(card) == 1 and cls.validate("h", card):
                return card
            elif len(card)==2 and cls.validate(card[0], card[1]):
                return card[1] 
         if isinstance(card, Card):
                return card.point
         return None
        
    def __repr__(self):
        return "<Card '%s'>" % (self.suit + self.point)

    # def __cmp__(self, otherCard):
    #     return cmp(self.rank, otherCard.rank)

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        pass

