import unittest
from blackjack.roles.human_player import BlackjackPlayer
from blackjack.elements.deck import PokerCard, PokerDeck


class TestBlackjackPlayer(unittest.TestCase):

    def test_create_player(self):
        my_test_player = BlackjackPlayer(name= 'John', starting_money=100)
        self.assertEqual('John', my_test_player.name)
        self.assertEqual(len(my_test_player.hand), 0)

    def test_get_card(self):
        my_test_player = BlackjackPlayer(name= 'John', starting_money=100)
        my_deck = PokerDeck()
        my_test_player.get_card(my_deck)
        self.assertEqual(len(my_test_player.hand), 1)
        self.assertIsInstance(my_test_player.hand[0], PokerCard)
