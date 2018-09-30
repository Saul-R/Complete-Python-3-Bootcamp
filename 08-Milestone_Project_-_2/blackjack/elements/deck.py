import random


class PokerCard:
    ALLOWED_SUITS = ['diamonds', 'spades', 'hearts', 'clubs']
    ALLOWED_VALUES = range(1, 14)

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        poker_value_dict = {
            1:  'Ace',
            2:  'Two',
            3:  'Three',
            4:  'Four',
            5:  'Five',
            6:  'Six',
            7:  'Seven',
            8:  'Eight',
            9:  'Nine',
            10: 'Ten',
            11: 'Jack',
            12: 'Queen',
            13: 'King',
        }

        print('{} of {}'.format(poker_value_dict[self.value]),self.suit)


class PokerDeck(object):
    def __init__(self):
        self.deck = [PokerCard(value, suit) for value in PokerCard.ALLOWED_VALUES for suit in PokerCard.ALLOWED_SUITS]
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()