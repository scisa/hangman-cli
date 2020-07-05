#!/usr/bin/env python3

import os.path

from game.Gameplay import Gameplay
from menu.ArgparseArgumentParser import ArgparseArgumentParser
from menu.MainMenu import MainMenu
from util.GlobalVariables import GlobalVariables


def is_none(arg):
    if arg is None:
        return True
    return False


def set_argument_variables(argument_parser):
    if not is_none(argument_parser.get_arguments().statistics):
        GlobalVariables.IS_PRINTING_STATISTICS = argument_parser.get_arguments().statistics
    if not is_none(argument_parser.get_arguments().level):
        GlobalVariables.REQUESTED_LEVEL = argument_parser.get_arguments().level
    if not is_none(argument_parser.get_arguments().play_now):
        GlobalVariables.IS_INSTANT_PLAYING = argument_parser.get_arguments().play_now


def calculate_options(option_id='play'):
    if option_id == 'play':
        game_play = Gameplay()
        game_play.play()
    elif option_id == 'exit':
        Gameplay.exit_game()


def start_with_menu():
    main_menu = MainMenu()
    main_menu.print_menu()
    option = main_menu.insert_option()

    if option is not None:
        calculate_options(option.get_id())
    else:
        calculate_options('exit')


def start_application():
    while True:
        GlobalVariables.MENU_COUNTER = GlobalVariables.LOWEST_INDEX_OF_MENU
        if not GlobalVariables.IS_INSTANT_PLAYING:
            start_with_menu()
        else:
            calculate_options()


if __name__ == '__main__':
    exec_file = os.path.abspath(__file__)
    GlobalVariables.SCRIPT_EXECUTION_PATH = os.path.abspath(__file__)[0:exec_file.rindex('/') + 1]

    parser = ArgparseArgumentParser()
    set_argument_variables(parser)

    start_application()
