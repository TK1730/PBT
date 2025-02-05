import tkinter as tk
import random
from pstats import Stats
from tkinter import messagebox

from pkg_resources import WorkingSet

from utils.pomodotimer import PomodoroTimer

class PomodoroWindow(tk.Tk):
    """
    Window表示用
    """
    def __init__(self, pomodoro_timer):
        super().__init__()

        self.title("Pomodoro Blackout Timer")
        self.geometry("500x500")

        self.pomodoro_timer = pomodoro_timer
        self.current_window = None  # 現在のウィンドウを保持

        self.show_start_window()

    def show_start_window(self):
        """
        スタートウィンドウ表示
        """
        self.change_window(StartWindow)
    
    def show_working_window(self):
        """
        作業ウィンドウ表示
        """
        self.change_window(WorkingWindow)

    def show_rest_window(self):
        """
        休憩ウィンドウ表示
        """
        self.change_window(RestWindow)

    def show_finish_window(self):
        """
        終了ウィンドウ表示
        """
        self.change_window(FinishWindow)

    def change_window(self, window):
        """
        ウィンドウ変更
        """
        if self.current_window is not None:
            self.current_window.destroy()

        self.current_window = window(self, self.pomodoro_timer)
        self.current_window.pack()



class StartWindow(tk.Frame):
    """
    スタートウィンドウ
    """
    def __init__(self, master, pomodoro_timer: PomodoroTimer):
        """
        スタートウィンドウに使用する変数
        """
        super().__init__(master)
        self.pomodoro_timer = pomodoro_timer

        self.title = "ポモドーロタイマー"
        self.subtitle = "限界を超えろ!"
        self.message = "作業時間を決めてね"
        self.start_button_text = "スタート"

        title_label = tk.Label(self, text=self.title, font=("Arial", 16))
        title_label.pack(pady=10)

        subtitle_label = tk.Label(self, text=self.subtitle, font=("Arial", 9))
        subtitle_label.pack(pady=5)

        message_label = tk.Label(self, text=self.message, font=("Arial", 9))
        message_label.pack(pady=5)

        self.user_input_box = tk.Entry(self, font=("Arial", 12))
        self.user_input_box.pack(pady=5)

        self.start_button = tk.Button(self, text=self.start_button_text, font=("Arial", 12), command=self.StartTimer)
        self.start_button.pack(pady=10)
    
    def StartTimer(self):
        # Timerクラスに総作業時間を代入
        self.pomodoro_timer.input_repeat(int(self.user_input_box.get()))
        self.master.show_working_window()


class WorkingWindow(tk.Frame):
    def __init__(self, master, pomodoro_timer: PomodoroTimer):
        """
            作業ウィンドウ
        """
        super().__init__(master)
        self.pomodoro_timer = pomodoro_timer

        self.message = "自分を超えろ！"
        message_label = tk.Label(self, text=self.message, font=("Arial", 9))
        message_label.pack(pady=5)

        # 作業時間を表示
        self.minutes, self.sec = self.pomodoro_timer.time_work.Transform()
        self.left_time_label = tk.Label(self, text=f"{self.minutes:2}:{self.sec:2}", font=("Arial", 20))
        self.left_time_label.pack(pady=10)

        self.left_lim_label = tk.Label(self, text=f"{self.pomodoro_timer.rep.rep_now} / {self.pomodoro_timer.rep.rep_limit}", font=("Arial", 9))
        self.left_lim_label.pack(pady=5)

        # 作業時間の更新
        self.update_timer()

    def update_timer(self):
        """
            タイマー更新
        """
        self.pomodoro_timer.time_work.CountDown()
        self.minutes, self.sec = self.pomodoro_timer.time_work.Transform()
        self.left_time_label.config(text=f"{self.minutes:2}:{self.sec:2}")
        self.left_lim_label.config(text=f"{self.pomodoro_timer.rep.rep_now} / {self.pomodoro_timer.rep.rep_limit}")

        if self.pomodoro_timer.time_work.currnet_time == 0:
            self.master.show_rest_window()
        else:
            self.after(1000, self.update_timer)

class RestWindow(tk.Frame):
    def __init__(self, master, pomodoro_timer: PomodoroTimer):
        """
        restウィンドウで使用する変数
        """
        super().__init__(master)
        self.pomodoro_timer = pomodoro_timer

        self.rest_methods = ["つむつむ","仮眠","休憩"]
        self.rest_way()

        # 休憩時のメッセージ表示
        self.message_label = tk.Label(self, text=f"休憩方法 : {self.chosen_method}", font=("Arial", 9))
        self.message_label.pack(pady=5)

        # 休憩時間を表示
        self.minutes, self.sec = self.pomodoro_timer.time_rest.Transform()
        self.left_time_label = tk.Label(self, text=f"{self.minutes:2} : {self.sec:2}", font=("Arial", 20))
        self.left_time_label.pack(pady=5)

        # 休憩時間の更新
        self.update_timer()

    def rest_way(self):
        """
        休憩方法を獲得
        """
        self.chosen_method = random.choice(self.rest_methods)
    
    def update_timer(self):
        """
        タイマー更新
        """
        self.pomodoro_timer.time_rest.CountDown()
        self.minutes, self.sec = self.pomodoro_timer.time_rest.Transform()
        self.left_time_label.config(text=f"{self.minutes:2}:{self.sec:2}")

        if self.pomodoro_timer.time_rest.currnet_time == 0:
            if self.pomodoro_timer.rep.flag_finish:
                self.master.show_finish_window()
            else:
                self.master.show_working_window()
        else:
            self.after(1000, self.update_timer)

class FinishWindow(tk.Frame):
    def __init__(self, master, pomodoro_timer: PomodoroTimer):
        """
        終了ウィンドウで使用する変数
        """
        super().__init__(master)
        self.pomo_timer = pomodoro_timer

        self.title = "お疲れさまでした"
        self.subtitle = "水分補給してゆっくり休みましょう"

        self.title_label = None
        self.subtitle_label = None
        self.title_label = tk.Label(self.root, text=self.title, font=("Arial", 30))
        self.title_label.pack(pady=5)

        self.subtitle_label = tk.Label(self.root, text=self.subtitle, font=("Arial",10))
        self.subtitle_label.pack(pady=5)

if __name__ == "__main__":
    pass


