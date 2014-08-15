from PaoDeKuai.card import Card
from PaoDeKuai.combination import *


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
      """
      print Sequence.extract(["sA","dA", "h3", "d3", "h4"])
      s1 = SequenceOfSingle(["sJ","sT","dQ", "hK", "d9"])
      s2 = SequenceOfSingle(["sJ","sT","dQ", "hK", "d9"])
      print s1 == s2