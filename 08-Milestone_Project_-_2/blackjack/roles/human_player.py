from blackjack.roles.player import BlackjackPlayer


class HumanPlayer(BlackjackPlayer):

    def play_turn(self):
       pass

    def can_bet(self, bet):
        return bet <= self.money





