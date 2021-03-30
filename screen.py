from os import system, name
from colorama import Fore, init
from cards import Card, Suit, Rank
import cards
from art import suits


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def draw_card(card: Card):
   rows = insert_rank(suits[card.suit], card.rank)
   for i in range(0, len(rows)):
        row = rows[i]
        print(row)

def insert_rank(rows, rank) -> list:
    clone = rows.copy()
    row = rows[1]
    clone[1] = row[0] + cards.rank_to_str(rank) + row[2:]
    return clone