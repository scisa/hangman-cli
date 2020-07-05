from util.Statistics import Statistics


class Winning:
    @classmethod
    def check_if_word_right(cls, word, guess):
        if str(word) == str(guess):
            cls.won()
            return True
        return False

    @classmethod
    def check_if_letters_all_right(cls, tf_list):
        if False not in tf_list:
            cls.won()
            return True
        return False

    @classmethod
    def won(cls):
        print("Congratulations you guessed the right word!")
        print()
        # Statistics.print_statistics()

    @classmethod
    def check_if_winning(cls, word, guess, is_word, tf_list):
        if is_word:
            return cls.check_if_word_right(word, guess)
        return cls.check_if_letters_all_right(tf_list)

