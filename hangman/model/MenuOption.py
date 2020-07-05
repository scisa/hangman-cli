from util.Color import Color
from util.GlobalVariables import GlobalVariables


class MenuOption:
    def __init__(self, id, title):
        self._id = id
        self._current_menu_counter = GlobalVariables.MENU_COUNTER
        self._index = self.get_current_menu_counter()
        self._title = title
        self._func = None
        GlobalVariables.MENU_COUNTER += 1

    def get_index(self):
        return self._index

    def get_title(self):
        return self._title

    def get_id(self):
        return self._id

    def set_func(self, func):
        self._func = func

    def get_current_menu_counter(self):
        return self._current_menu_counter

    def exec_func(self):
        self._func()

    def print_option(self, color=Color.BLUE, text_style=''):
        print(color, text_style, str(self.get_index()), ":", str(self.get_title()), Color.WHITE)