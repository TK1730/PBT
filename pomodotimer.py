import utils.timer as timer
import utils.repeat as repeat

class PomodoroTimer(object):
    def __init__(self):
        # フェーズの状態
        self.phase = 1
        
        # ウィンドウ
        self.window_start = 1
        self.window_working = 2
        self.window_rest = 3
        self.window_finish = 4

        # ポモドーロの時間設定
        self.time_work = timer.TimeWork(25)
        self.time_rest = timer.TimeRest(5)

        # 繰り返し
        self.rep = None

    def __call__(self, *args, **kwds):
        while(self.phase):
            if self.phase == 1:
                pass
            elif self.phase == 2:
                pass
            elif self.phase == 3:
                pass
            elif self.phas == 4:
                pass


    def start_phase(self):
        print("input hours")
        x = input()
        print(type(x))

if __name__ == '__main__':
    pomo = PomodoroTimer()
    pomo.start_phase()