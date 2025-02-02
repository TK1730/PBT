import tkinter as tk
import random
from pstats import Stats
from tkinter import messagebox

from pkg_resources import WorkingSet

<<<<<<< HEAD

class PomodoroWindow(object):
=======
import utils.timer as timer

class PomodoroWindow(tk.Tk):
>>>>>>> feature-app
    """
    Window表示用
    """
    def __init__(self):
<<<<<<< HEAD
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
=======
        super().__init__()

        self.title("Pomodoro Blackout Timer")
        self.geometry("500x500")

        # すべてのフレームを辞書に保存
        self.frames = {}

        # フレーム（ウィンドウ）を作成
        self.frames = {}

        # 作業用タイマー
        self.work_timer = timer.TimeWork(25)
        # 休憩用タイマー
        self.frames = timer.TimeRest(5)

        # フレーム（ウィンドウ）を作成
        for F in (StartWindow, WorkingWindow, RestWindow, FinishWindow):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartWindow)
    
    def show_frame(self, page: tk.Frame):
        """
            指定したページを表示する
        Args:
            page ( window ): windowのクラス
        """
        frame = self.frames[page]
        frame.tkraise()



class StartWindow(tk.Frame):
    """
    スタートウィンドウ
    """
    def __init__(self, master):
        """
        スタートウィンドウに使用する変数
        """
        super().__init__(master)
>>>>>>> feature-app

        self.title = "ポモドーロタイマー"
        self.subtitle = "限界を超えろ!"
        self.message = "作業時間を決めてね"
        self.start_button_text = "スタート"
<<<<<<< HEAD
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
=======

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
        timer.Timer.set_total_time(self.user_input_box.get())
        self.master.show_frame(WorkingWindow)


class WorkingWindow(tk.Frame):
    def __init__(self, master):
        """
            作業ウィンドウ
        """
        super().__init__(master)

        self.message = "自分を超えろ！"
        message_label = tk.Label(self, text=self.message, font=("Arial", 9))
        message_label.pack(pady=5)

        self.left_time_label = tk.Label(self, text="", font=("Arial", 20))
        self.left_time_label.pack(pady=10)

        self.left_lim_label = tk.Label(self, text=f"{now_lim} / {left_lim}", font=("Arial", 9))
        self.left_lim_label.pack(pady=5)

    def update_timer(self):
        pass
>>>>>>> feature-app

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
<<<<<<< HEAD
    window.start_window(20)
=======
    window.start_window()
    work = timer.TimeWork(25)
    print(work.total_time)
    print("Finish")
>>>>>>> feature-app


