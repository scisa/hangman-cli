import argparse


class ArgparseArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.arguments = None
        self.define_argument_parser()

    def add_arguments(self):
        self.parser.add_argument("-s", "--statistics", help="print statistics after game", action="store_true")
        self.parser.add_argument("-l", "--level", type=int, choices=[0, 1, 2],
                            help="define level of difficulty from easy to hard [0-2]; default is 1 for middle")
        self.parser.add_argument("-p", "--play_now", help="instant playing without main menu at first time",
                                 action="store_true")

    def define_argument_parser(self):
        self.add_arguments()
        self.arguments = self.parser.parse_args()

    def get_arguments(self):
        return self.arguments
