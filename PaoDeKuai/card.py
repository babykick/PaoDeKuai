


class Card:
    RANK = {'3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '10':8,
            "J":9, "Q":10, "K":11, "A":12, "2":13}
    comparor = None
    
    def __init__(self, cardName=None, suit=None, point=None):
        s, p = None, None
        if cardName and not point and not suit:    
           s, p  = cardName[0], cardName[1]
        elif not cardName and point and suit:
           s, p = suit, point
        if not self.validate(suit=s, point=p):
            raise Exception("Card name is not valid")
        self.suit = s
        self.point = p
        
        
    @classmethod
    def validate(self, suit, point):
        return (point in Card.RANK.keys()) and (suit in ["s", "c", "h", "d"])
        
    @property    
    def point(self):
        return self.point
    
    @property
    def rank(self):
        return self.getRank(self.point)
     
    @classmethod 
    def getRank(cls, point):
        return Card.RANK.get(point)
     
    @property
    def suit(self):
        return self.suit
    
    @classmethod
    def setComparor(cls, comp):
        cls.comparor = comp
        
    
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
        return self.suit + self.point

    def __cmp__(self, otherCard):
        return cmp(self.rank, otherCard.rank)
        
