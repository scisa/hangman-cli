import random

from util.GlobalVariables import GlobalVariables


class Word:
    def __init__(self):
        self._word = ''
        try:
            with open(GlobalVariables.SCRIPT_EXECUTION_PATH + 'words.txt', 'r') as file:
                word_list = [line.rstrip('\n') for line in file]
        except IOError:
            print("No words.txt file for getting words found in Directory " + GlobalVariables.SCRIPT_EXECUTION_PATH)
            print("Using standard word to work")
            word_list = [GlobalVariables.DEFAULT_WORD]

        index = random.randint(0, len(word_list) - 1)
        self._word = word_list[index]
        self._len_word = len(self._word)

    def __repr__(self):
        return self.get_word()

    def get_word(self):
        return self._word
