from util.Color import Color
from util.GlobalVariables import GlobalVariables
from util.TextStyle import TextStyle


class Statistics:
    current_level = 0
    count_of_trys = 0

    @classmethod
    def print_statistics(cls):
        if GlobalVariables.IS_PRINTING_STATISTICS:
            cls.print_startistics_art(TextStyle.UNDERLINE + "Statistics")
            cls.print_startistics_art("You played on Level: " + str(Statistics.current_level))
            cls.print_startistics_art("You needed: " + str(Statistics.count_of_trys) + " trys.")
            print()

    @classmethod
    def print_startistics_art(cls, msg):
        print(Color.GREEN, msg, Color.WHITE)

    @classmethod
    def reset_statistics(cls):
        cls.current_level = 0
        cls.count_of_trys = 0