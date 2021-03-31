from cards import Rank, Card
from itertools import product

score_map = {
    Rank.ace: [1, 11],
    Rank.two: [2],
    Rank.three: [3],
    Rank.four: [4],
    Rank.five: [5],
    Rank.six: [6],
    Rank.seven: [7],
    Rank.eight: [8],
    Rank.nine: [9],
    Rank.ten: [10],
    Rank.jack: [10],
    Rank.queen: [10],
    Rank.king: [10],
    }

def calc_score(card_list: list) -> list:
    ranks = list(map(lambda c: c.rank, card_list))
    return calc_score_by_ranks(ranks) 


def calc_score_by_ranks(ranks: list) -> list:
    rank_values = list(map(lambda r: score_map[r], ranks))
    prods = list(product(*rank_values))
    scores = list(map(lambda t: sum(t), prods))
    return scores