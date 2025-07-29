import utils.timer as timer
import utils.GUI as gui
import utils.repeat as repeat
import time

class PomodoroTimer(object):
    def __init__(self, work_time: int = 25, rest_time: int = 5):
        # ポモドーロの時間設定
        self.time_work = timer.TimeWork(work_time)
        self.time_rest = timer.TimeRest(rest_time)

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