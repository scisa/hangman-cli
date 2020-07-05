from util.GlobalVariables import GlobalVariables

from util.Statistics import Statistics


class Death:
    @classmethod
    def is_dead(cls, current_progress, word):
        if current_progress.get_progress() > GlobalVariables.MAX_BEFORE_DEATH:
            print("You are dead!")
            print("The word you searched for is: ", word)
            print()
            Statistics.print_statistics()
            return True
        return False