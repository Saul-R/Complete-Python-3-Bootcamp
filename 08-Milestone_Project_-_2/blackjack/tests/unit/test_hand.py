import unittest

from blackjack.elements.hand import BlackjackHand
from blackjack.elements.card import PokerCard


class TestHand(unittest.TestCase):
    def test_create_hand(self):
        test_hand = BlackjackHand()
        self.assertEqual(test_hand.value, 0)
        self.assertEqual(len(test_hand.cards), 0)

    def test_add_card(self):
        test_hand = BlackjackHand()
        test_card = PokerCard(1, 'hearts')
        test_hand.add_card(test_card)
        self.assertEqual(len(test_hand.cards), 1)
        self.assertEqual(test_hand.value, 11)

    def test_hands_value(self):
        expected_results = [
            [[10, 11], 20],
            [[10, 12], 20],
            [[10, 13], 20],
            [[1, 10], 21],
            [[1, 10, 11], 21],
            [[2, 3, 11, 13], 0],
            [[1, 1, 1, 1, 12, 5], 19]
        ]
        for card_values, expected_value in expected_results:
            test_hand = BlackjackHand()
            for card_value in card_values:
                test_hand.add_card(PokerCard(card_value, 'clubs'))
            self.assertEqual(expected_value, test_hand.value)
