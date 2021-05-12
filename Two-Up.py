playagain = "yes"
while (playagain == "yes"):

    from Game import Game

    class TwoUp:
        def __init__(self):
            self.game = Game()


        def main_function(self):
            self.game.make_guess()
            self.game.flip_coin_1()
            self.game.flip_coin_2()
            self.game.check_guess();

    twoUp = TwoUp()
    twoUp.main_function()
    continue
