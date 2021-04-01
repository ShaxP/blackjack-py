import pytest
from score_calculator import calc_score_by_ranks, calc_score, formatted_score
from cards import Rank, Card, Suit

@pytest.mark.parametrize("ranks, expected_score", 
[
    ([Rank.two, Rank.eight], 10), 
    ([Rank.seven], 7),
    ([Rank.ace, Rank.two], 13),
    ([Rank.ace, Rank.two], 3),
    ([Rank.king, Rank.nine], 19)
]
)
def test_calc_score_by_rank(ranks, expected_score):
    scores = calc_score_by_ranks(ranks)
    assert expected_score in scores


@pytest.mark.parametrize("card_list, expected_score", 
[
    ([Card(Suit.diamond, Rank.two), Card(Suit.spade, Rank.eight)], 10), 
    ([Card(Suit.diamond, Rank.seven)], 7), 
    ([Card(Suit.club, Rank.ace), Card(Suit.heart, Rank.two)], 13),
    ([Card(Suit.club, Rank.ace), Card(Suit.spade, Rank.two)], 3),
    ([Card(Suit.heart, Rank.king), Card(Suit.diamond, Rank.nine)], 19),
    ([Card(Suit.spade, Rank.ace, True), Card(Suit.heart, Rank.two)], 2),
]
)
def test_calc_score(card_list, expected_score):
    scores = calc_score(card_list)
    assert expected_score in scores

@pytest.mark.parametrize("card_list, expected_score", 
[
    ([Card(Suit.diamond, Rank.two), Card(Suit.spade, Rank.eight)], "10"), 
    ([Card(Suit.diamond, Rank.seven)], "7"), 
    ([Card(Suit.club, Rank.ace), Card(Suit.heart, Rank.two)], "3, 13"),
    ([Card(Suit.heart, Rank.king), Card(Suit.diamond, Rank.nine)], "19"),
    ([Card(Suit.spade, Rank.ace, True), Card(Suit.heart, Rank.two)], "2"),
    ([Card(Suit.spade, Rank.ace), Card(Suit.heart, Rank.king)], "21"),
    ([Card(Suit.spade, Rank.ace), Card(Suit.heart, Rank.nine), Card(Suit.diamond, Rank.five)], "15"),
    ([Card(Suit.spade, Rank.ace), Card(Suit.heart, Rank.nine), Card(Suit.diamond, Rank.five), Card(Suit.diamond, Rank.six)], "21"),
    ([Card(Suit.spade, Rank.ace), Card(Suit.heart, Rank.nine), Card(Suit.diamond, Rank.five), Card(Suit.diamond, Rank.seven)], "22"),
]
)
def test_formatted_score(card_list, expected_score):
    score = formatted_score(card_list)
    assert score == expected_score
