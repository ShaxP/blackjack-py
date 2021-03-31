from enum import IntEnum, Enum
from collections import namedtuple

class Suit(IntEnum):
    spade = 0
    club = 1
    diamond = 2
    heart = 3

class Rank(Enum):
    ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13

class Card:
    def __init__(self, suit, rank, conceiled=False):
        self.suit = suit
        self.rank = rank
        self.conceiled = conceiled
    
    def conceil(self):
        self.conceiled = True
    
    def reveal(self):
        self.conceiled = False

rank_map = {
    Rank.ace: 'A',
    Rank.two: '2',
    Rank.three: '3',
    Rank.four: '4',
    Rank.five: '5',
    Rank.six: '6',
    Rank.seven: '7',
    Rank.eight: '8',
    Rank.nine: '9',
    Rank.ten: '10',
    Rank.jack: 'J',
    Rank.queen: 'Q',
    Rank.king: 'K',
    }

def rank_to_str(rank):
    return rank_map[rank]


class Deck:
    def __init__(self, number_of_decks=1):
        self._cards = [Card(suit, rank, False) 
            for suit in Suit
            for rank in Rank] * number_of_decks

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, card):
        self._cards[position] = card

    def __delitem__(self, position):
        del self._cards[position]