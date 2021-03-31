import pytest
from score_calculator import calc_score_by_ranks
from cards import Rank

@pytest.mark.parametrize("ranks, expected_score", 
[
    ([Rank.two, Rank.eight], 10), 
    ([Rank.seven], 7),
    ([Rank.ace, Rank.two], 13),
    ([Rank.ace, Rank.two], 3),
    ([Rank.king, Rank.nine], 19)
]
)
def test_score_calc(ranks, expected_score):
    scores = calc_score_by_ranks(ranks)
    assert expected_score in scores