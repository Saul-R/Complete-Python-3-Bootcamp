import unittest
from blackjack.elements.deck import *


class TestPokerDeck(unittest.TestCase):

    def test_create_deck(self):
        my_test_deck = PokerDeck()
        self.assertIsInstance(my_test_deck.deck[0], PokerCard)

    def test_deal_card(self):
        my_test_deck = PokerDeck()
        dealt_card = my_test_deck.deal_card()
        deck_size = len(PokerCard.ALLOWED_SUITS) * len(PokerCard.ALLOWED_VALUES)
        self.assertIsInstance(dealt_card, PokerCard)
        self.assertEqual(len(my_test_deck.deck), (deck_size - 1))

