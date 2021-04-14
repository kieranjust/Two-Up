from Game import Game


class TwoUp:
    def __init__(self):
        self.game = Game()

    def play():
        playagain = "no";
        while (playagain != "no"):
            print("Do you want to play again")
            playagain = input()
            if (playagain == "no"):
                break
            else:
                continue
                

    def main_function(self):
        self.game.make_guess()
        self.game.flip_coin_1()
        self.game.flip_coin_2()
        self.game.check_guess()
        self.game.score()
        self.game.play()



twoUp = TwoUp()
twoUp.main_function()