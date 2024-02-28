import random
from player import Player 

class Cards(object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    SUITS = ('SPADES', 'CLUBS', 'HEARTS', 'DIAMONDS')
    def __init__ (self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return str(self.suit) + " " + str(self.rank)

class Deck(object):
    def __init__(self):
        self.deck = []
        for suit in Cards.SUITS:
            for rank in Cards.RANKS:
                card = Cards(rank, suit)
                self.deck.append(card)

    def __str__(self):
        deckList = ""
        i = 0
        for card in self.deck:
            deckList = deckList + str(card) + " " + str(i) + "\n"
            i = i + 1
        return deckList

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

class Dealer(object):
    def __init__(self, deck):
        self.deck = deck

    # TODO: get players' list -> distribute one by one.
    def distribute(self, player : Player):
        for i in range (2):
            if len(self.deck) is not 0:
                player.hand.append(self.deck.deck.pop(0))
