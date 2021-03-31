import pytest
from cards import Card, Rank, Suit
import screen
from art import suits

ace_of_club = [
    ".------.",
    "|A __  |",
    "| (  ) |",
    "|(_  _)|",
    "| /__\\ |",
    "`------´",
    ]

ten_of_club = [
    ".------.",
    "|10__  |",
    "| (  ) |",
    "|(_  _)|",
    "| /__\\ |",
    "`------´",
    ]

king_of_spade =[
    ".------.",
    "|K /\\  |",
    "| /  \\ |",
    "|(_  _)|",
    "| /__\\ |",
    "`------´",
]

two_of_spade =[
    ".------.",
    "|2 /\\  |",
    "| /  \\ |",
    "|(_  _)|",
    "| /__\\ |",
    "`------´",
]

jack_of_diamond = [
    ".------.",
   r"|J /\  |",
   r"| /  \ |",
   r"| \  / |",
   r"|  \/  |",
    "`------´",
]

seven_of_diamond = [
    ".------.",
    "|7 /\\  |",
    "| /  \\ |",
    "| \\  / |",
    "|  \\/  |",
    "`------´",
]

queen_of_heart = [
    ".------.",
    "|Q_  _ |",
    "|( \\/ )|",
    "| \\  / |",
    "|  \\/  |",
    "`------´",
]

nine_of_heart = [
    ".------.",
    "|9_  _ |",
    "|( \\/ )|",
    "| \\  / |",
    "|  \\/  |",
    "`------´",
]

@pytest.mark.parametrize("suit,rank,to_compare", [
    (Suit.club, Rank.ace, ace_of_club),
    (Suit.club, Rank.ten, ten_of_club),
    (Suit.spade, Rank.king, king_of_spade),
    (Suit.spade, Rank.two, two_of_spade),
    (Suit.diamond, Rank.jack, jack_of_diamond),
    (Suit.diamond, Rank.seven, seven_of_diamond),
    (Suit.heart, Rank.queen, queen_of_heart),
    (Suit.heart, Rank.nine, nine_of_heart),
])
def test_insert_rank(suit, rank, to_compare):
    # Arrange
    # card = Card(suit= Suit.club, rank= Rank.ace)
    rows = suits[suit]
    # Act
    card_rows = screen.insert_rank(rows, rank)
    # Assert
    assert card_rows == to_compare
