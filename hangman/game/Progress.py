
class Progress:
    def __init__(self):
        self._progress = 0

    def inc_progress(self, number=1):
        self._progress += number

    def check_progress(self, tf):
        if tf is False:
            return self.inc_progress()

    def get_progress(self):
        return self._progress

    def reset_progress(self):
        self._progress = 0

    def set_progress(self, current_progress):
        self._progress = current_progress

    def draw_progress(self, stages):
        stage = stages.get_stage()
        print(self.return_if_progress('    _______________', stage[9]))
        print(self.return_if_progress('    ||            ', stage[8]) + self.return_if_progress('|', stage[10]))
        print(self.return_if_progress('    ||            ', stage[7]) + self.return_if_progress('O', stage[11]))
        print(self.return_if_progress('    ||           ', stage[6]) + self.return_if_progress('\\|/', stage[12]))
        print(self.return_if_progress('    ||            ', stage[5]) + self.return_if_progress('|', stage[13]))
        print(self.return_if_progress('    ||           ', stage[4]) + self.return_if_progress('/ \\', stage[14]))
        print(self.return_if_progress('    ||', stage[3]))
        print(self.return_if_progress('  ######', stage[2]))
        print(self.return_if_progress(' #      #', stage[1]))
        print(self.return_if_progress('#        #', stage[0]))
        print("\n")

    def return_if_progress(self, to_print, current_progress):
        if self._progress >= current_progress:
            return to_print
        else:
            return ''
