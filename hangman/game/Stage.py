from util.GlobalVariables import GlobalVariables
from util.Statistics import Statistics


class Stage:
    def __init__(self, level=2):
        self._level = level
        self._stage = []
        self.set_stage()
        self.set_death()
        Statistics.current_level = self.get_level()

    def set_low(self):
        self._stage = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def set_middle(self):
        self._stage = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]

    def set_high(self):
        self._stage = [1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]

    def get_stage(self):
        return self._stage

    def get_level(self):
        return self._level

    def set_death(self):
        GlobalVariables.MAX_BEFORE_DEATH = self.get_stage()[-1]

    def set_stage(self):
        if self.get_level() == 0:
            self.set_low()
        elif self.get_level() == 1:
            self.set_middle()
        else:
            self.set_high()