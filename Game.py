import random


class Game:
    def __init__(self):
        self.__coin1 = ''
        self.__coin2 = ''
        self.__outcome = ''
        self.__player_guess = ''
        self.__correct_guesses = 0
        self.__amount_of_guesses = 0

    def make_guess_heads_heads(self):
        """Sets the players guess to heads, heads"""
        self.__player_guess = "HH"

    def make_guess_heads_tails(self):
        """Sets the players guess to heads, tails"""
        self.__player_guess = "HT"

    def make_guess_tails_tails(self):
        """Sets the players guess to tails, tails"""
        self.__player_guess = "TT"

    def flip_coin_1(self):
        """Flips the first coin using the random number generator. 0 == heads, 1 == tails"""
        if random.randint(0, 1) == 0:
            self.__coin1 = "H"
            return self.__coin1
        else:
            self.__coin1 = "T"
            return self.__coin1

    def flip_coin_2(self):
        """Flips the second coin using the random number generator. 0 == heads, 1 == tails"""
        if random.randint(0, 1) == 0:
            self.__coin2 = "H"
            return self.__coin2
        else:
            self.__coin2 = "T"
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



            if self.__outcome == self.__player_guess:
                self.__correct_guesses = self.__correct_guesses + 1;
                self.__amount_of_guesses = self.__amount_of_guesses + 1
                print("You have guessed {0} out of {1} correctly".format(self.__correct_guesses, self.__amount_of_guesses))

            else:
                self.__amount_of_guesses = self.__amount_of_guesses + 1
                print("You have guessed {0} out of {1} correctly".format(self.__correct_guesses, self.__amount_of_guesses))

