from cards import Deck, Card
from random import shuffle
from enum import Enum
import screen
from score_calculator import calc_score, formatted_score, final_score

class GameState(Enum):
    quit = 0
    ongoing = 1
    player_wins = 2
    player_blackjack = 3
    dealer_wins = 4
    draw = 5
    out_of_balance = 6

class Game:
    def __init__(self):
        self._deck = Deck(8)
        shuffle(self._deck)
        self._current_card_index = 0
        self._game_state = GameState.ongoing

    def _new_game(self):
        self._dealers_turn = True
        self._dealers_hand = []
        self._players_hand = []
        self._game_state = GameState.ongoing
        self._dealer_score = []
        self._player_score = []
        self._deal(alternate=True)
        self._deal(alternate=True)
        self._deal(conceiled=True, alternate=True)
        self._deal()
    
    def _next_card(self, conceiled=False) -> Card:
        next_card = self._deck[self._current_card_index]
        next_card.conceiled = conceiled
        self._current_card_index += 1
        return next_card
    
    def _deal(self, conceiled=False, alternate=False):
        hand = self._dealers_hand if self._dealers_turn else self._players_hand
        hand.append(self._next_card(conceiled))

        if self._dealers_turn:
            self._update_dealer_score()
        else:
            self._update_player_score()

        self._check_game_status()

        if alternate:
            self._dealers_turn = not self._dealers_turn

    def _is_ongoing(self): 
        return self._game_state == GameState.ongoing
    
    def _update_balance(self):
        if self._game_state == GameState.player_wins:
            self._balance += self._bet
        elif self._game_state == GameState.player_blackjack:
            self._balance += self._bet * 3 // 2
        elif self._game_state == GameState.dealer_wins:
            self._balance -= self._bet
        if self._balance <= 0:
            self._game_state = GameState.out_of_balance

    def _check_game_status(self):
        if self._dealers_turn:
            if self._final_dealer_score == 21:
                self._game_state = GameState.dealer_wins
                self._update_balance()
            elif self._final_dealer_score > 21:
                self._game_state = GameState.player_wins
                self._update_balance()
            elif self._final_dealer_score > 17:
                self._game_state = GameState.player_wins if self._final_dealer_score < self._final_player_score else GameState.dealer_wins
                self._update_balance()
        else:
            if self._final_player_score == 21:
                self._game_state = GameState.player_blackjack if len(self._players_hand) == 2 else GameState.player_wins
                self._update_balance()
            elif self._final_player_score > 21:
                self._game_state = GameState.dealer_wins
                self._update_balance()

    def _reveal_dealers_card(self):
        self._dealers_hand[1].reveal()
        self._update_dealer_score()
        self._check_game_status()
        self._draw_table()

    def _update_dealer_score(self):
        self._dealer_score = calc_score(self._dealers_hand)
        self._final_dealer_score = final_score(self._dealers_hand)
        self._dealer_formatted_score = formatted_score(self._dealers_hand)

    def _update_player_score(self):
        self._player_score = calc_score(self._players_hand)
        self._final_player_score = final_score(self._players_hand)
        self._player_formatted_score = formatted_score(self._players_hand)

    def _print_dealer_score(self):
        print(f"Dealer score: {self._dealer_formatted_score if self._is_ongoing() else self._final_dealer_score}")
    
    def _print_player_score(self):
        print(f"Your score: {self._final_player_score if self._dealers_turn else self._player_formatted_score}")

    def _print_player_balance(self):
        print(f"Balance: ${self._balance}   Bet: ${self._bet}")

    def _print_results(self):
        if self._game_state == GameState.player_wins:
            print("You win😊 Nice job👏")
        elif self._game_state == GameState.dealer_wins:
            print("Dealer wins! Better luck next time.")

    def _draw_table(self):
        screen.clear()
        screen.draw_cards(self._dealers_hand)
        self._print_dealer_score()
        print("\n\n")
        screen.draw_cards(self._players_hand)
        self._print_player_score()
        self._print_player_balance()
        print("\n")
        if not self._is_ongoing():
            self._print_results()


    def play(self):
        screen.print_logo()
        self._balance = int(input("How much money you want to buy chips with? $"))
        self._bet = int(input("Place your bet: 10, 20 or 50: $"))
        
        while self._game_state != GameState.quit:
            self._new_game()
            self._draw_table()

            while self._is_ongoing():
                command = input("\n[h]it or [s]tand?: ")
                if command.lower() == "h":
                    self._deal()
                    self._draw_table()
                else:
                    self._dealers_turn = True
                    break
            if self._is_ongoing():
                if self._dealers_hand[1].conceiled:
                    self._reveal_dealers_card()
                while self._is_ongoing():
                    self._deal()
                    self._draw_table()
            
            if self._game_state == GameState.out_of_balance:
                print("You ran out of money☹️ Game over!!!")
                break

            command = input('[s]ame bet, new [b]et or [q]uit?: ')
            if command.lower() == "q":
                _game_state = GameState.quit
                print("Goodbye👋 Hope to see you soon!")
                break
            elif command.lower() == "b":
                self._bet = int(input("New bet: 10, 20 or 50: $"))
            else:
                self._new_game()
