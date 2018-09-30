import unittest
from blackjack.roles.human_player import BlackjackPlayer


class TestBlackjackPlayer(unittest.TestCase):

    def test_create_player(self):
        my_test_player = BlackjackPlayer(name= 'John', starting_money=100)
        self.assertEqual('John', my_test_player.name)
