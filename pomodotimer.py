import utils.timer as timer
import utils.repeat as repeat



class PomodoroTimer(object):
    def __init__(self):
        # フェーズの状態
        self.phase = {0: "start_menu",
                      1: "work_meenu",
                      2: "rest_menu",
                      3: "finish_menu"}
        # 現在のフェーズ
        self.current_phase = 0
        # ポモドーロの時間設定
        self.time_work = timer.TimeWork(25)
        self.time_rest = timer.TimeRest(5)

    def change_phase(self):
        pass
        


    def change_window(self):
        self.phase[self.current_phase]
    