from cards import Deck, Card, Suit, Rank
import pytest

@pytest.mark.parametrize("order,expected_card", 
[
    (0, Card(Suit.spade, Rank.ace, False)),
    (10, Card(Suit.spade, Rank.jack, False)),
    (14, Card(Suit.club, Rank.two, False)),
    (24, Card(Suit.club, Rank.queen, False)),
    (26, Card(Suit.diamond, Rank.ace, False)),
    (33, Card(Suit.diamond, Rank.eight, False)),
    (44, Card(Suit.heart, Rank.six, False)),
    (51, Card(Suit.heart, Rank.king, False)),
])
def test_a_card_in_deck(order, expected_card):
    # Arrange
    deck = Deck()
    # Act

    # Assert
    assert deck[order] == expected_card


def test_delete_a_card():
    # Arrange
    deck = Deck()
    # Act
    del deck[0]
    # Assert 
    assert deck[0] == Card(Suit.spade, Rank.two, False)

@pytest.mark.parametrize("number_of_decks,expected_no_cards", 
[
    (1, 52),
    (2, 104),
    (3, 156),
    (4, 208),
    (5, 260),
    (6, 312),
    (7, 364),
    (8, 416)
]
)
def test_number_of_cards(number_of_decks, expected_no_cards):
    deck =  Deck(number_of_decks)
    assert len(deck) == expected_no_cards
