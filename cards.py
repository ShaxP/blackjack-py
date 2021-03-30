from enum import IntEnum
from collections import namedtuple

class Suit(IntEnum):
    spade = 0
    club = 1
    diamond = 2
    heart = 3

class Rank(IntEnum):
    ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    jack = 10
    queen = 10
    king = 10

Card = namedtuple('Card', ('suit','rank'))

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
    Rank.jack: 'J',
    Rank.queen: 'Q',
    Rank.king: 'K',
    }

def rank_to_str(rank):
    return rank_map[rank] 