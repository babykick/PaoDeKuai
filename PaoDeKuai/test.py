from card import Card
from combination import SingleCard, PairTwo


if __name__ == "__main__":
      c = Card("d4")
      print Card.onlyPoint(c)
      
      c2 = Card("h4")
      print c == c2
      sc = SingleCard([Card("d4")])
      sc2 = SingleCard("sA")
      print sc > sc2
      pair = PairTwo(["s2","h2"])