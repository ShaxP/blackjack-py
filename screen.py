from os import system, name
from colorama import Fore, init
from cards import Card, Suit, Rank
import cards
from art import suits, conceiled, logo


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def draw_card(card: Card):
   rows = conceiled if card.conceiled else insert_rank(suits[card.suit], card.rank) 
   for i in range(0, len(rows)):
        row = rows[i]
        print(row)

def insert_rank(rows, rank) -> list:
    clone = rows.copy()
    row = rows[1]
    rank_str = cards.rank_to_str(rank)
    clone[1] = row[0] + rank_str + row[len(rank_str) + 1:]

    return clone

def merge_cards(card_list) -> list:
    assert len(card_list) != 0
    card_suits = list(map(lambda c: conceiled if c.conceiled else insert_rank(suits[c.suit], c.rank), card_list))
    result = []
    for i in range(0, len(card_suits[0])):
        row = []
        for suit in card_suits:
            row.append(suit[i])
        result.append("  ".join(row))
    return result

def draw_cards(card_list):
    rows = merge_cards(card_list)
    for row in rows:
        print(row)

def print_logo():
    clear()
    print(logo)