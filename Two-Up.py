import tkinter
import tkinter as tk
from breezypythongui import EasyFrame
from Game import Game
game = Game()
N = tkinter.N
S = tkinter.S
E = tkinter.E
W = tkinter.W


class TwoUp(EasyFrame):
    def __init__(self):
        self.game = Game()
        EasyFrame.__init__(self, title="Two-Up",
                           width="550", height="210")
        self.addLabel(text="Make your bet by clicking one of the three buttons and then clicking the check guess button"
                           ".",
                      row=0, column=0, columnspan=2)


        button_panel = self.addPanel(row=1, column=0, columnspan=2)
        button_panel.addButton(text="HH", row=0, column=0, command=self.heads_heads_handler)
        button_panel.addButton(text="HT", row=0, column=1, command=self.heads_tails_handler)
        button_panel.addButton(text="TT", row=0, column=2, command=self.tails_tails_handler)
        # Having issues centering the text fields with the row and column counts. Had to stretch with E + W
        self.guessField = self.addTextField(text="", row=2, column=0, sticky=N + S, state='disabled')

        self.addButton(text="Check guess",
                       row=3, column=0,
                       command=self.check_guess_handler)
        # Having issues centering the text fields with the row and column counts. Had to stretch with E + W
        # Fixed issues where textfield is now set to read only
        self.outputField1 = self.addTextField(text="", row=4, column=0, sticky=N + S, state='disabled')
        # Having issues centering the text fields with the row and column counts. Had to stretch with E + W
        self.outputField2 = self.addTextField(text="", row=5, column=0, sticky=N + S, state='disabled')
        # Having issues centering the text fields with the row and column counts. Had to stretch with E + W
        self.outputField3 = self.addTextField(text="", row=6, column=0, sticky=E + W, state='disabled')

    def heads_heads_handler(self):
        game.make_guess_heads_heads()
        self.guessField.setText("HH")
        self.game.make_guess_heads_heads()

    def heads_tails_handler(self):
        game.make_guess_heads_tails()
        self.guessField.setText("HT")
        self.game.make_guess_heads_tails()

    def tails_tails_handler(self):
        game.make_guess_tails_tails()
        self.guessField.setText("TT")
        self.game.make_guess_tails_tails()

    def check_guess_handler(self):
        self.outputField1.setText(self.game.flip_coin_1())
        self.outputField2.setText(self.game.flip_coin_2())
        self.outputField3.setText(self.game.check_guess())


twoUp = TwoUp().mainloop()
