from game.Death import Death
from game.Progress import Progress
from game.Stage import Stage
from game.UserInput import UserInput
from game.Winning import Winning
from model.Word import Word
from util.GlobalVariables import GlobalVariables
from util.Statistics import Statistics


class Gameplay:
    def __init__(self):
        self._word_to_guess = Word()
        self._stage = Stage(GlobalVariables.REQUESTED_LEVEL)
        self._progress = Progress()
        self._user_input = UserInput(self.get_word_to_guess())

    def check_if_dead(self, is_letter_guessed):
        self.get_progress().check_progress(is_letter_guessed)
        is_dead = Death.is_dead(self.get_progress(), self.get_word_to_guess())

        return is_dead

    def play(self):
        while True:
            # User input
            self.get_progress().draw_progress(self.get_stage())
            self.get_user_input().print_guessing_line(self.get_word_to_guess())
            self.get_user_input().print_past_guesses_level(self.get_stage())
            guess = self.get_user_input().input_guess()
            is_word = UserInput.is_word(guess)

            # Check user input
            is_letter_guessed = self.get_user_input().check_if_letter_true(guess, self.get_word_to_guess())

            # Test for Winning
            is_winning = Winning.check_if_winning(self.get_word_to_guess(), guess, is_word,
                                                  self.get_user_input().get_word_tf_list())
            if is_winning:
                break

            # Test for losing
            is_dead = self.check_if_dead(is_letter_guessed)

            if is_dead:
                break

        Statistics.reset_statistics()


    @classmethod
    def exit_game(cls):
        exit(0)

    def get_word_to_guess(self):
        return self._word_to_guess

    def get_stage(self):
        return self._stage

    def get_progress(self):
        return self._progress

    def get_user_input(self):
        return self._user_input
