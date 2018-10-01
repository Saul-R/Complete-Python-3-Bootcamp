from blackjack.elements.card import PokerCard
from functools import reduce


class BlackjackHand(object):
    def __init__(self):
        self.cards = []
        self.value = 0
        self.bust = False

    @staticmethod
    def max_in_blackjack(x, y):
        if x > 21 and y <= 21:
            return y
        elif x <= 21 and y > 21:
            return x
        else:
            return max(x, y)

    def add_card(self, card):
        self.cards.append(card)
        self._calculate_value()

    def _calculate_value(self):
        possible_scores = [0]
        for card in self.cards:
            if (card.value <= 10) and (card.value >= 2):
                possible_scores = list(map(lambda x: x + card.value, possible_scores))
            elif card.value > 10:
                possible_scores = list(map(lambda x: x + 10, possible_scores))
            elif card.value == 1:
                possible_scores = list(map(lambda x: x + 11, possible_scores)) + \
                                  list(map(lambda x: x + 1, possible_scores))

        self.value = reduce(self.max_in_blackjack, possible_scores)
        if self.value > 21:
            self.value = 0
            print("BUST!")
            self.bust = True


