


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
        self.reset()
        for card in exclude: self.cards.remove(card)


    def reset(self):
        self.cards = [index for index in range(1,55,1)]

    def removeCard(self, cardInd):
        self.cards.remove(cardInd)

    def shuffle(self):
        random.shuffle(self.cards)

    def dispatchHands(self, divideNum):
        if len(self.cards) % divideNum != 0:
           raise Exception("The card can not divided equally")

        cards = [Card(self._getCardFace(index), self._getCardSuit(index)) for index in self.cards]
        each = len(cards)/divideNum
        result = []
        start = 0
        for i in range(divideNum):
           h = Hand()
           h.addCards(cards[start:start + each ])
           result.append(h)
           start += each

        return result

    def _getCardFace(self, index):
        return self.CARDFACE.get((index-1) % 13)

    def _getCardSuit(self, index):
        return self.SUIT.get((index-1) / 13)

    def __repr__(self):
        return repr(self.cards)

class Hand:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def addCards(self,cards):
        self.cards.extend(cards)

    def play(self, cardsStr):
        pattern = Pattern(cardsStr)
        for c in pattern.getCards():
            self.cards.remove(c)


    def sort(self):
        self.cards.sort()

    def __str__(self):
        return repr(self.cards)

    def toString(self):
        return repr(self.cards)