from cards import Deck, Card
from random import shuffle
from enum import Enum
import screen

class GameState(Enum):
    ongoing = 1
    finished = 2
    quit = 3

class Game:
    def __init__(self):
        self._deck = Deck(8)
        shuffle(self._deck)
        self._current_card_index = 0
        self.new_game()

    def _next_card(self, conceiled=False) -> Card:
        next_card = self._deck[self._current_card_index]
        next_card.conceiled = conceiled
        self._current_card_index += 1
        return next_card

    def deck(self) -> Deck:
        return self._deck
    
    def deal(self, conceiled=False, alternate=False):
        hand = self._delears_hand if self._dealers_turn else self._players_hand
        hand.append(self._next_card(conceiled))
        if alternate:
            self._dealers_turn = not self._dealers_turn

    def new_game(self):
        self._dealers_turn = True
        self._delears_hand = []
        self._players_hand = []
        self._game_state = GameState.ongoing
        self.deal(alternate=True)
        self.deal(alternate=True)
        self.deal(conceiled=True, alternate=True)
        self.deal()

    def _draw_table(self):
        screen.clear()
        screen.draw_cards(self._delears_hand)
        print("\n\n")
        screen.draw_cards(self._players_hand)

    def play(self):
        screen.print_logo()

        while self._game_state != GameState.quit:
            self._draw_table()
            if not self._dealers_turn:
                command = input("\n[h]it or [s]tand?: ")
                if command.lower() == "h":
                    self.deal()
                    self._draw_table()
                else:
                    self._dealers_turn = True
            else:
                if self._delears_hand[1].conceiled:
                    self._delears_hand[1].reveal()
                    self._draw_table()
                command = input('\nAnother one? y or n: ')
                if command.lower() == "n":
                    _game_state = GameState.quit
                    break
                else:
                    self.new_game()
