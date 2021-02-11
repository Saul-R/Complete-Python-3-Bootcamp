from blackjack.elements.deck import PokerDeck
from blackjack.roles.human_player import HumanPlayer
from blackjack.roles.machine_dealer import MachineDealer


def initialize_game(player, dealer, game_deck):
    player.new_hand()
    dealer.new_hand()
    player.get_card(game_deck)
    dealer.get_card(game_deck)
    player.get_card(game_deck)
    dealer.get_card(game_deck)


def play_a_game(player, dealer):
    game_deck = PokerDeck()
    initialize_game(player, dealer, game_deck)
    while True:
        initial_bet = input("Place initial bet: ")
        if initial_bet > player.money:
            print("Your mouth makes promises your wallet cant take")
    player.print_hand()
    while not player.hand.bust:
        input()

if __name__ == "__main__":
    keep_playing = "yes"
    player_name = input('What is your name?: ')
    player_balance = int(input('How much money do you want to bet?: '))

    player = HumanPlayer(name=player_name, starting_money=player_balance)
    dealer = MachineDealer()
    while keep_playing == "yes":
        play_a_game(player,dealer)
        keep_playing = input('Play Again? (yes / no): ')
    print('Thanks for playing.')
