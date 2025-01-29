import tkinter as tk
import random
from pstats import Stats
from tkinter import messagebox

from pkg_resources import WorkingSet


class PomodoroWindow(object):
    """
    Window表示用
    """
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pomodoro Blackout Timer")
        self.root.geometry("500x500")


class StartWindow(PomodoroWindow):
    """
    スタートウィンドウ
    """
    def __init__(self):
        """
        スタートウィンドウに使用する変数
        """
        super().__init__()

        self.title = "ポモドーロタイマー"
        self.subtitle = "限界を超えろ!"
        self.message = "作業時間を決めてね"
        self.start_button_text = "スタート"
        self.user_input_box = None
        self.start_button = None


    def start_window(self, usr_input):
        """
        スタートウィンドウが表示される
        """
        title_label = tk.Label(self.root, text=self.title, font=("Arial", 16))
        title_label.pack(pady=10)

        subtitle_label = tk.Label(self.root, text=self.subtitle, font=("Arial", 9))
        subtitle_label.pack(pady=5)

        message_label = tk.Label(self.root, text=self.message, font=("Arial", 9))
        message_label.pack(pady=5)

        self.user_input_box = tk.Entry(self.root, font=("Arial", 12))
        self.user_input_box.pack(pady=5)

        self.start_button = tk.Button(self.root, text=self.start_button_text, font=("Arial", 12), command=usr_input)
        self.start_button.pack(pady=10)

        self.root.mainloop()


class WorkingWindow(PomodoroWindow):
    """
    作業中ウィンドウ
    """
    def __init__(self):
        """
        作業中ウィンドウに使用する変数
        """
        super().__init__()

        self.message = "自分を超えろ！"
        self.left_time_label = None
        self.left_lim_label = None

    def working_window(self, minutes, sec, now_lim, left_lim):

        """
        作業中ウィンドウの表示
        """
        message_label = tk.Label(self.root, text=self.message, font=("Arial", 9))
        message_label.pack(pady=5)

        self.left_time_label = tk.Label(self.root, text=f"{minutes} : {sec}", font=("Arial", 20))
        self.left_time_label.pack(pady=10)

        self.left_lim_label = tk.Label(self.root, text=f"{now_lim} / {left_lim}", font=("Arial", 9))
        self.left_lim_label.pack(pady=5)

        self.root.mainloop()

class RestWindow(PomodoroWindow):
    """
    休憩中ウィンドウ
    """
    def __init__(self):
        """
        restウィンドウで使用する変数
        """
        super().__init__()

        self.rest_methods = ["つむつむ","仮眠","休憩"]

        self.left_time_label = None
        self.message_label = None

    def rest_window(self, minutes, sec):
        """
        休憩中ウィンドウ表示
        """
        self.rest_way()

        self.message_label = tk.Label(self.root, text=f"休憩方法　:　{self.chosen_method}", font=("Arial", 9))
        self.message_label.pack(pady=5)

        self.left_time_label = tk.Label(self.root, text=f"{minutes} : {sec}", font=("Arial", 20))
        self.left_time_label.pack(pady=5)

        self.root.mainloop()

    def rest_way(self):
        """
        休憩方法を獲得
        """
        self.chosen_method = random.choice(self.rest_methods)

class FinishWindow(PomodoroWindow):
    """
    終了ウィンドウ
    """
    def __init__(self):
        """
        終了ウィンドウで使用する変数
        """
        super().__init__()

        self.title = "お疲れさまでした"
        self.subtitle = "水分補給してゆっくり休みましょう"

        self.title_label = None
        self.subtitle_label = None

    def finish_window(self):
        """
        終了ウィンドウ表示
        """
        self.title_label = tk.Label(self.root, text=self.title, font=("Arial", 30))
        self.title_label.pack(pady=5)

        self.subtitle_label = tk.Label(self.root, text=self.subtitle, font=("Arial",10))
        self.subtitle_label.pack(pady=5)

        self.root.mainloop()

if __name__ == "__main__":
    window = StartWindow()
    window.start_window(20)


