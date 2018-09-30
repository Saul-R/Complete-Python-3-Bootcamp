from blackjack.elements.deck import PokerDeck


class BlackjackPlayer(object):

    def __init__(self, name, starting_money):
        self.hand = []
        self.money = starting_money
        self.name = name

    def introduce_myself(self):
        print("Nice to meet you, I am {}".format(self.name))

    def get_card(self,current_deck):
        self.hand.append(current_deck.deal_card())

    def show_hand(self):
        print()
