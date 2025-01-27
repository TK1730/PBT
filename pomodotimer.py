import utils.timer as timer
import utils.repeat as repeat
import time

class PomodoroTimer(object):
    def __init__(self):
        # フェーズの状態
        self.phase = 1
        
        # ウィンドウ
        self.window_start = 1  # 初めの画面
        self.window_working = 2  # 作業画面
        self.window_rest = 3  # 休憩画面
        self.window_finish = 4  # 終わりの画面

        # ポモドーロの時間設定
        self.time_work = timer.TimeWork(25)
        self.time_rest = timer.TimeRest(5)

        # 繰り返し
        self.rep = None

    def __call__(self, *args, **kwds):
        if self.phase == 1:
            self.start_phase()
            
            while input("start? (y/n): ").lower() != 'y':
                print("まだだよーん")
            
            self.phase = 2
            print("変更")

        elif self.phase == 2:
            print("phase 2")
            self.work_phase()
            self.phase = 3

        elif self.phase == 3:
            print("phase 3")
            self.rest_phase(self.time_rest)
            self.time_rest.ResetTime()

        elif self.phas == 4:
            pass

    def start_phase(self):
        """

        """
        print("input hours")
        self.rep = repeat.Repeat(int(input()))

    def pomodoro_phase(self, t:timer.Timer):
        while t.seconds >= 0:
            print(t.seconds)
            t.CountDown()
            time.sleep(1)
        


if __name__ == '__main__':
    pomo = PomodoroTimer()
    pomo()