

class card(object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    SUITS = ('SPADES', 'CLUBS', 'HEARTS', 'DIAMONDS')
    def __init__ (self, rank, suit):
        self.rank = rank
        self.suit = suit