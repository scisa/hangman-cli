
from error_handling.Exceptions import Exceptions
from model.MenuOption import MenuOption
from util.Color import Color
from util.GlobalVariables import GlobalVariables
from util.TextStyle import TextStyle


class MainMenu:
    def __init__(self):
        self._title = 'H A N G M A N - Main Menu'
        self._options_list = self.get_options()

    def print_menu_title(self, color=Color.MAGENTA, text_style=TextStyle.BOLD):
        print(color, text_style, str(self.get_title()), Color.WHITE)

    def print_options(self):
        for option in self.get_options_list():
            option.print_option()

    def print_menu(self):
        self.print_menu_title()
        self.print_options()

    def get_options(self):
        options_list = []
        new_game = MenuOption('play', 'New Game')
        options_list.append(new_game)
        exit_game = MenuOption('exit', "Exit Game")
        options_list.append(exit_game)

        return options_list

    def get_option_from_index(self, index):
        return self.get_options_list()[index]

    def insert_option(self):
        index = input("Please choose an option by index: ")
        index = Exceptions.menu_insert_check_exception(index)
        if index != GlobalVariables.LOWEST_INDEX_OF_MENU - 1:
            return self.option_chosen(index)
        return None

    def option_chosen(self, index):
        option = self.get_option_from_index(index)
        return option

    def get_title(self):
        return self._title

    def get_options_list(self):
        return self._options_list


