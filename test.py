from PaoDeKuai.card import Card
from PaoDeKuai.combination import *
from PaoDeKuai.hand import Deck, Hand
from PaoDeKuai.player import HumanPlayer
from PaoDeKuai.game import Game


if __name__ == "__main__":
      """
      c = Card("d4")
      print Card.onlyPoint(c)
      
      c2 = Card("h4")
      print c == c2
      sc = SingleCard([Card("d4")])
      sc2 = SingleCard("sA")
      print sc > sc2
      pair = PairTwo(["s2","h2"])
      
      print Sequence.extract(["sA","dA", "h3", "d3", "h4"])
      s1 = SequenceOfSingle(["sJ","sT","dQ", "hK", "d9"])
      s2 = SequenceOfSingle(["sJ","sT","dQ", "hK", "dA", "s9"])
     
      print Bomb.validate(["sJ", "dJ", "hJ","h3"])
      
      d = Deck()
      d.shuffle()
      hands = d.dispatch(3)
      player1 = HumanPlayer("Mike")
      player2 = HumanPlayer("Stephen")
      player3 = HumanPlayer("John")
      player1.giveHand(hands[0])
      player2.giveHand(hands[1])
      player3.giveHand(hands[2])
      """
      g = Game(deckset = "PaoDeKuai")
      g.addPlayer(HumanPlayer("mike"))
      g.addPlayer(HumanPlayer("Stephen"))
      g.addPlayer(HumanPlayer("John"))
      g.setup()
      g.start()
      