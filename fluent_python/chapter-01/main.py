from collections import namedtuple


Card = namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(s) for s in range(1, 11)] + list("JQKA")
    suits = "spreads diamond heart club".split()

    def __init__(self) -> None:
        self._cards = [Card(r, s) for r in self.ranks for s in self.suits]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card(5, 'diamond')
print(beer_card)
deck = FrenchDeck()
for card in reversed(deck):
    print(card)