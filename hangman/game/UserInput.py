from game.Winning import Winning
from util.Statistics import Statistics


class UserInput:
    def __init__(self, word):
        self._past_guesses = []
        self._word_tf_list = [False] * len(word.get_word())

    def input_guess(self):
        guess = str(input("Insert the word or a letter that might be right: ")).strip()
        self.add_guess_to_past_guesses(guess)

        return guess

    def check_if_print_letter(self, tf, letter):
        if tf is True:
            print(letter + " ", end='')
        else:
            print("_ ", end='')

    def print_guessing_line(self, word):
        for index, letter in enumerate(str(word)):
            tf = self.get_index_of_tf_list(index)
            self.check_if_print_letter(tf, letter)
        print("\n\n")

    def add_guess_to_past_guesses(self, guess):
        self.append_to_past_guesses(guess)
        Statistics.count_of_trys += 1

    def append_to_past_guesses(self, guess):
        self._past_guesses.append(guess)

    def get_past_guesses(self):
        return self._past_guesses

    @classmethod
    def current_stage_for_print(cls, stage):
        return ' --- Level: ' + str(stage.get_level())

    def print_past_guesses_level(self, stage):
        if len(self.get_past_guesses()) > 0:
            print("Your past guesses: ", self.get_past_guesses(), self.current_stage_for_print(stage))
        else:
            print(self.current_stage_for_print(stage))
        print()

    def get_word_tf_list(self):
        return self._word_tf_list

    def get_index_of_tf_list(self, index):
        return self._word_tf_list[index]

    @classmethod
    def is_word(cls, guess):
        if len(guess) > 1:
            return True
        return False

    def check_if_letter_true(self, guess, word):
        is_true = False
        for index, letter in enumerate(str(word)):
            if str(letter) == str(guess):
                is_true = True
                self.set_index_true(index)
        return is_true

    def set_index_true(self, index):
        self._word_tf_list[index] = True






class UserInputBak:
    def __init__(self):
        self._word = word
        self._current_progress = current_progress
        self._current_stage = stage
        self._past_guesses = []
        self._word_tf_list = [False] * self.get_word().get_len_word()

    def get_word(self):
        return self._word

    def get_word_tf_list(self):
        return self._word_tf_list

    def get_index_of_tf_list(self, index):
        return self._word_tf_list[index]

    def add_guess_to_past_guesses(self, guess):
        self._past_guesses.append(guess)
        Statistics.count_of_trys += 1

    def get_past_guesses(self):
        return self._past_guesses

    def set_index_true(self, index):
        self._word_tf_list[index] = True

    def get_current_progress(self):
        return self._current_progress

    def get_current_stage(self):
        return self._current_stage

    def current_stage_for_print(self):
        return ' --- Level: ' + str(self.get_current_stage().get_level())

    def check_if_letter_true(self, guess):
        is_true = False
        for index, letter in enumerate(str(self.get_word())):
            if str(letter) == str(guess):
                is_true = True
                self.set_index_true(index)
        return is_true

    def check_winning(self, is_true):
        if is_true:
            Winning.check_if_letters_all_right(self.get_word_tf_list())

    def is_word(self, guess):
        if len(guess) > 1:
            return True
        return False

    def print_past_guesses_level(self):
        if len(self.get_past_guesses()) > 0:
            print("Your past guesses: ", self.get_past_guesses(), self.current_stage_for_print())
            print("\n")
        else:
            print(self.current_stage_for_print())

    def input_guess(self):
        self.print_past_guesses_level()
        guess = str(input("Insert the word or a letter that might be right: ")).strip()
        self.add_guess_to_past_guesses(guess)

        return guess

    def check_if_print_letter(self, tf, letter):
        if tf is True:
            print(letter + " ", end='')
        else:
            print("_ ", end='')

    def print_guessing_line(self):
        for index, letter in enumerate(str(self.get_word())):
            tf = self.get_index_of_tf_list(index)
            self.check_if_print_letter(tf, letter)
        print("\n\n")
