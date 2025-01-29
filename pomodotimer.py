import utils.timer as timer
import utils.GUI as gui
import utils.repeat as repeat
import time

class PomodoroTimer(object):
    def __init__(self):
        # フェーズの状態
        self.phase = 1

        # ウィンドウフェーズ
        self.window_start = gui.StartWindow()  # 初めの画面
        self.window_working = gui.WorkingWindow()  # 作業画面
        self.window_rest = gui.RestWindow()  # 休憩画面
        self.window_finish = gui.FinishWindow()  # 終わりの画面

        # ポモドーロの時間設定
        self.time_work = timer.TimeWork(25)
        self.time_rest = timer.TimeRest(5)

        # 繰り返し
        self.rep = None

    def __call__(self, *args, **kwds):
        self.window_start.start_window(1)

    def start_phase(self):
        """

        """
        self.window_start.start_window(5)

    def pomodoro_phase(self, t:timer.Timer):
        while t.seconds >= 0:
            print(t.seconds)
            t.CountDown()
            time.sleep(1)
        


if __name__ == '__main__':
    pomo = PomodoroTimer()
    pomo()