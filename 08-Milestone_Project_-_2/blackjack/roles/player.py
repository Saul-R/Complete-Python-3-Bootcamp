from blackjack.elements.deck import PokerDeck


class BlackjackPlayer(object):

    def __init__(self, name, starting_money):
        self.hand = []
        self.money = starting_money
        self.name = name

    def introduce_myself(self):
        print("Nice to meet you, I am {}".format(self.name))

    def get_card(self, current_deck):
        cart_dealt = current_deck.deal_card()
        self.hand.append(cart_dealt)

    def print_hand(self):
        print("=======")
        for card in self.hand:
            print(card)
        print("=======")

    def win_money(self, earnings):
        self.money += earnings

    def lose_money(self, loses):
        if self.money < loses:
            print("Can't lose that much money!")
            raise ValueError
        else:
            self.money -= loses
