from cards import Suit, Rank, Card, Deck
from game import Game
import screen
from random import shuffle

# screen.clear()
# screen.print_logo()
# card_list = [
#     Card(Suit.club, Rank.ten, False), 
#     Card(Suit.heart, Rank.ten, False),
#     Card(Suit.diamond, Rank.ten, False),
#     Card(Suit.spade, Rank.ten, False)
# ]

# screen.draw_cards(card_list)

game = Game()
game.play()