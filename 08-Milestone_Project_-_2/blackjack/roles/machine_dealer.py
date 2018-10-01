from blackjack.roles.player import BlackjackPlayer


class MachineDealer(BlackjackPlayer):

    def __init__(self):
        super().__init__(name='DEALER', starting_money=999999)

