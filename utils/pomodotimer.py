import utils.timer as timer
import utils.GUI as gui
import utils.repeat as repeat
import time

class PomodoroTimer(object):
    def __init__(self):
        # ポモドーロの時間設定
        self.time_work = timer.TimeWork(25)
        self.time_rest = timer.TimeRest(5)

        # 繰り返し
        self.rep = None

    def input_repeat(self, hours: int):
        """
        繰り返し回数を入力
        """
        self.rep = repeat.Repeat(hours)

if __name__ == '__main__':
    pomo = PomodoroTimer()
    pomo()