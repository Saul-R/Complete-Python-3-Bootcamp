import random
from blackjack.elements.card import PokerCard


class PokerDeck(object):
    def __init__(self):
        self.deck = [PokerCard(value, suit) for value in PokerCard.ALLOWED_VALUES for suit in PokerCard.ALLOWED_SUITS]
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
