

class BlackjackPlayer(object):

    def __init__(self, name, starting_money):
        self.hand = []
        self.money = starting_money
        self.name = name

    def introduce_myself(self):
        print("Nice to meet you, I am {}".format(self.name))


def test_method():
    print('This is just a test method')


if __name__ == "__main__":
    my_test_player = BlackjackPlayer(name='John', starting_money=100)
    my_test_player.introduce_myself()
