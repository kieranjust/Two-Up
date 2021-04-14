import random





class Game:
    def __init__(self):
        self.__coin1 = ''
        self.__coin2 = ''
        self.__outcome = ''
        self.__player_guess = ''

    def make_guess(self):
        """Asks the player to guess what the coins will land on. Inputs can be 'HH' 'HT' or 'TT case insensitive"""
        while not (self.__player_guess == 'HH' or self.__player_guess == 'HT' or self.__player_guess == 'TT'):
            print("What is your guess? ('HH', 'HT' or 'TT')")
            self.__player_guess = input().upper()

    def flip_coin_1(self):
        """Flips the first coin using the random number generator. 0 == heads, 1 == tails"""
        if random.randint(0, 1) == 0:
            self.__coin1 = "H"
            print("The first coin landed on heads.")
            return self.__coin1
        else:
            self.__coin1 = "T"
            print("The first coin landed on tails.")
            return self.__coin1

    def flip_coin_2(self):
        """Flips the second coin using the random number generator. 0 == heads, 1 == tails"""
        if random.randint(0, 1) == 0:
            self.__coin2 = "H"
            print("The second coin landed on heads.")
            return self.__coin2
        else:
            self.__coin2 = "T"
            print("The second coin landed on tails.")
            return self.__coin2

    def check_guess(self):
        """Checks the player guess with the outcome of the coin flips and generates a message based on outcome"""
        self.__outcome = self.__coin1 + self.__coin2
        "This removes the chance of TH equalling an incorrect guess if HT is guessed"
        if self.__outcome == 'TH':
            self.__outcome = 'HT'

        if self.__outcome == self.__player_guess:
            print("Congratulations, you guessed correctly!")
        else:
            print("Sorry your guess was incorrect!")

    def score(self):
            """Keeps track of the player score if he wants to play again"""
            highscore = 0;
            if self.__outcome == self.__player_guess:
                highscore = highscore + 1;
                print("Your score is " + str(highscore))

            else:
                print("Your score is " + str(highscore))

    def play(self):
        playagain = "no";
        while (playagain != "no"):
            print("Do you want to play again")
            playagain = input()
            if (playagain == "no"):
                break
            else:
                continue