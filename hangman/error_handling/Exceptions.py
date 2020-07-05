from model.MenuOption import MenuOption
from util.Color import Color
from util.GlobalVariables import GlobalVariables


class Exceptions:
    @classmethod
    def print_error(cls, msg):
        print(Color.RED, str(msg))

    @classmethod
    def menu_insert_check_exception(cls, insert):
        try:
            insert = int(insert)
            if GlobalVariables.LOWEST_INDEX_OF_MENU > insert > MenuOption.menu_counter:
                raise ValueError
            return insert
        except ValueError:
            cls.print_error("not a valid option")
            return GlobalVariables.LOWEST_INDEX_OF_MENU - 1
