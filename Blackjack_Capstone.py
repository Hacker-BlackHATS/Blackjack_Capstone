# Blackjack Project

"""
Our Blackjack House Rules
  1>  The deck is unlimited in size.
  2>  There are no jokers.
  3>  The Jack/Queen/King all count as 10.
  4>  The the Ace can count as 11 or 1.
  5>  Use the following list as the deck of cards:
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  6>  The cards in the list have equal probability of being drawn.
  7>  Cards are not removed from the deck as they are drawn.
  8>  The computer is the dealer.
"""

from art import blackjack_logo as logo
from random import choices, choice
from Other_functions import clear


def result(user_sum, computer_sum):
    """User cards sum, Computer cards sum"""
    if user_sum > 21:
        print("You lose.")
    elif computer_sum > 21:
        print("You win.")
    elif user_sum == computer_sum:
        print("It's a draw.")
    elif user_sum > computer_sum:
        print("You win.")
    else:
        print("You lose.")


def game():
    """Play Blackjack/21 game"""
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = [11, 11]
    computer_cards = choices(population=cards, k=2)
    want_another = 'y'
    while want_another == 'y':
        print(f"Your cards: {user_cards}")
        print(f"Computer's first card: {computer_cards[0]}")
        want_another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if want_another == 'y':
            user_cards.append(choice(cards))
    if want_another == 'n':
        user_s = sum(user_cards)
        if user_s > 21 and 11 in user_cards:
            user_cards[user_cards.index(11)] = 1
            user_s = sum(user_cards)
        print(f"Your final hand: {user_cards}")
        if sum(computer_cards) < 17:
            computer_cards.append(choice(cards))
        print(f"Computer's final hand: {computer_cards}")
        computer_s = sum(computer_cards)
        result(user_s, computer_s)


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while play == 'y':
    game()
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    clear()
