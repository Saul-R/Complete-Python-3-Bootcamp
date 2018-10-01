import unittest
from blackjack.roles.human_player import HumanPlayer
from blackjack.roles.machine_dealer import MachineDealer
from blackjack.roles.player import BlackjackPlayer
from blackjack.elements.deck import PokerCard, PokerDeck


class TestBlackjackPlayer(unittest.TestCase):

    def test_create_player(self):
        my_test_player = BlackjackPlayer(name='John', starting_money=100)
        self.assertEqual('John', my_test_player.name)
        self.assertEqual(len(my_test_player.hand), 0)

    def test_get_card(self):
        my_test_player = BlackjackPlayer(name='John', starting_money=100)
        my_deck = PokerDeck()
        my_test_player.get_card(my_deck)
        self.assertEqual(len(my_test_player.hand), 1)
        self.assertIsInstance(my_test_player.hand[0], PokerCard)

    def test_money_changes(self):
        my_test_player = BlackjackPlayer(name='John', starting_money=100)
        self.assertRaises(ValueError, lambda: my_test_player.lose_money(101))
        my_test_player.lose_money(99)
        self.assertEqual(my_test_player.money, 1)
        my_test_player.win_money(10)
        self.assertEqual(my_test_player.money, 11)


class TestPlayer(unittest.TestCase):

    def test_create_player(self):
        my_test_player = HumanPlayer(name='John', starting_money=100)
        self.assertEqual('John', my_test_player.name)
        self.assertEqual(len(my_test_player.hand), 0)

    def test_get_card(self):
        my_test_player = HumanPlayer(name='John', starting_money=100)
        my_deck = PokerDeck()
        my_test_player.get_card(my_deck)
        self.assertEqual(len(my_test_player.hand), 1)
        self.assertIsInstance(my_test_player.hand[0], PokerCard)

    def test_money_changes(self):
        my_test_player = HumanPlayer(name='John', starting_money=100)
        self.assertRaises(ValueError, lambda: my_test_player.lose_money(101))
        my_test_player.lose_money(99)
        self.assertEqual(my_test_player.money, 1)
        my_test_player.win_money(10)
        self.assertEqual(my_test_player.money, 11)
        
        
class TestDealer(unittest.TestCase):

    def test_create_player(self):
        my_test_player = MachineDealer()
        self.assertEqual('DEALER', my_test_player.name)
        self.assertEqual(len(my_test_player.hand), 0)

    def test_get_card(self):
        my_test_player = MachineDealer()
        my_deck = PokerDeck()
        my_test_player.get_card(my_deck)
        self.assertEqual(len(my_test_player.hand), 1)
        self.assertIsInstance(my_test_player.hand[0], PokerCard)

    def test_money_changes(self):
        my_test_player = MachineDealer()
        my_test_player.lose_money(99)
        self.assertEqual(my_test_player.money, 999900)
        my_test_player.win_money(10)
        self.assertEqual(my_test_player.money, 999910)