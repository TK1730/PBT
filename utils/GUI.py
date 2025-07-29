import tkinter as tk
import time
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
        # self.geometry("500x500")
        self.state("zoomed")
        self.configure(bg="white")

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
        self.attributes("-fullscreen", False)
        self.iconify()
        self.change_window(WorkingWindow)

    def show_rest_window(self):
        """
        休憩ウィンドウ表示
        """
        self.attributes("-fullscreen", True)
        self.attributes("-topmost", True)
        self.deiconify()
        self.configure(bg="black")
        self.change_window(RestWindow)

    def show_finish_window(self):
        """
        終了ウィンドウ表示
        """
        self.attributes("-fullscreen", False)
        self.deiconify()
        self.state("zoomed")
        self.configure(bg="white")
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
        super().__init__(master, bg="white")
        self.pomodoro_timer = pomodoro_timer

        # ウィンドウ表示用変数
        self.title = "ポモドーロタイマー"
        self.subtitle = "限界を超えろ!"
        self.message = "作業時間を決めてね"
        self.start_button_text = "Start"

        # フォントサイズ
        font_tile = 130
        font_subtitle = 90
        font_user_input = 60

        # タイトル 
        title_label = tk.Label(self, text=self.title, font=("Arial", font_tile, "bold"), fg="blue", bg="white")
        title_label.pack(pady=(100, 10))

        # サブタイトル
        subtitle_label = tk.Label(self, text=self.subtitle, font=("Arial", font_subtitle, "bold"), bg="white")
        subtitle_label.pack(pady=(10, 160))

        # ユーザー入力ボックス
        self.user_input_box = tk.Entry(self, font=("Arial", font_user_input, "bold"), fg="grey", justify="center", highlightthickness=5, highlightcolor="orange")
        self.user_input_box.pack(pady=10)
        self.user_input_box.insert(0, self.message)
        self.user_input_box.bind("<FocusIn>", self.clear_placeholder)
        self.user_input_box.bind("<FocusOut>", self.add_placeholder)

        # スタートボタン
        self.start_button = tk.Button(self, text=self.start_button_text, font=("Arial", font_user_input, "bold"), command=self.starttimer, fg='white', bg='red')
        self.start_button.pack(pady=10)

    def clear_placeholder(self, event):
        """
        プレースホルダーをクリア
        """
        if self.user_input_box.get() == self.message:
            self.user_input_box.delete(0, tk.END)
            self.user_input_box.config(fg="black")

    def add_placeholder(self, event):
        """
        プレースホルダーを追加
        """
        if not self.user_input_box.get():
            self.user_input_box.insert(0, self.message)
            self.user_input_box.config(fg="grey")

    def starttimer(self):
        # Timerクラスに総作業時間を代入
        self.pomodoro_timer.input_repeat(int(self.user_input_box.get()))
        self.master.show_working_window()


class WorkingWindow(tk.Frame):
    def __init__(self, master, pomodoro_timer: PomodoroTimer):
        """
            作業ウィンドウ
        """
        super().__init__(master,bg="white")
        self.pomodoro_timer = pomodoro_timer

        # ウィンドウ表示用変数
        self.message = "自分を超えろ！"

        # フォントサイズ
        font_message = 90
        font_left_time_label = 200

        message_label = tk.Label(self, text=self.message, font=("Arial",  font_message),bg="white")
        message_label.pack(pady=(80,10), expand=True, fill=tk.BOTH)

        # 作業時間を表示
        self.minutes, self.sec = self.pomodoro_timer.time_work.Transform()
        self.left_time_label = tk.Label(self, text=f"{self.minutes:02}:{self.sec:02}", font=("Arial", font_left_time_label, 'bold'),
                                         highlightthickness=20, highlightcolor="orange", highlightbackground="orange", fg="orange",bg="white", padx=200, pady=50)
        self.left_time_label.pack(pady=50, expand=True, fill=tk.BOTH)

        # 作業回数を表示
        self.left_lim_label = tk.Label(self, text=f"{self.pomodoro_timer.rep.rep_now} / {self.pomodoro_timer.rep.rep_limit}", font=("Arial", 90, 'bold'),bg="white")
        self.left_lim_label.pack(expand=True, fill=tk.BOTH)

        # 作業時間の更新
        self.update_timer()

    def update_timer(self):
        """
            タイマー更新
        """
        self.start_time = time.time()
        self.pomodoro_timer.time_work.CountDown()
        self.minutes, self.sec = self.pomodoro_timer.time_work.Transform()
        self.left_time_label.config(text=f"{self.minutes:02}:{self.sec:02}")

        if self.pomodoro_timer.time_work.currnet_time == 0:
            self.pomodoro_timer.time_work.ResetTime()
            self.pomodoro_timer.rep.repeat_count()
            self.master.show_rest_window()
        else:
            delay = self.get_elapsed_time(self.start_time)
            self.after(delay, self.update_timer)
        

    def get_elapsed_time(self, start_time):
        """
            1秒との差を取得
        """
        one_sec = 1000
        elapsed_time = one_sec - int(time.time() - start_time) * one_sec
        delay = max(0, int(elapsed_time))
        return delay

class RestWindow(tk.Frame):
    def __init__(self, master, pomodoro_timer: PomodoroTimer):
        """
        restウィンドウで使用する変数
        """
        super().__init__(master, bg="black")
        self.pomodoro_timer = pomodoro_timer

        # 休憩方法
        self.rest_methods = ["仮眠","ストレッチ","水分補給","トイレ","散歩","軽いエクササイズ","遠くを見る","目を温める","好きな音楽を聞く","リラックスできるコンテンツを見る","日記やメモを書く","部屋の喚起","スナックタイム","飲み物などを準備する"]
        self.rest_way()

        # フォントサイズ
        font_message_label = 30
        font_left_time_label = 300

        # 休憩時のメッセージ表示
        self.message_label = tk.Label(self, text=f"休憩方法 : {self.chosen_method}", font=("Arial", font_message_label, 'bold'), bg="black", fg="white")
        self.message_label.pack(pady=(80,10), expand=True, fill="both")

        # 休憩時間を表示
        self.minutes, self.sec = self.pomodoro_timer.time_rest.Transform()
        self.left_time_label = tk.Label(self, text=f"{self.minutes:2} : {self.sec:2}", font=("Arial", font_left_time_label, 'bold'), highlightthickness=20, highlightcolor="white", highlightbackground="white", fg="white",bg="black", padx=200, pady=50)
        self.left_time_label.pack(pady=50, expand=True, fill="both")

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
        self.start_time = time.time()
        self.pomodoro_timer.time_rest.CountDown()
        self.minutes, self.sec = self.pomodoro_timer.time_rest.Transform()
        self.left_time_label.config(text=f"{self.minutes:02}:{self.sec:02}")

        if self.pomodoro_timer.time_rest.currnet_time == 0:
            self.pomodoro_timer.time_rest.ResetTime()
            if self.pomodoro_timer.rep.completion_judg():
                self.master.show_finish_window()
            else:
                self.master.show_working_window()
        else:
            delay = self.get_elapsed_time(self.start_time)
            self.after(delay, self.update_timer)

    def get_elapsed_time(self, start_time):
        """
            1秒との差を取得
        """
        one_sec = 1000
        elapsed_time = one_sec - int(time.time() - start_time) * one_sec
        delay = max(0, int(elapsed_time))
        return delay

class FinishWindow(tk.Frame):
    def __init__(self, master, pomodoro_timer: PomodoroTimer):
        """
        終了ウィンドウで使用する変数
        """
        super().__init__(master, bg="white")
        self.pomo_timer = pomodoro_timer

        # ウィンドウ表示用
        self.title = "お疲れさまでした"
        self.subtitle = "水分補給してゆっくり休みましょう"
        self.restart_button_text = "まだまだやるぞ！"

        # フォントサイズ
        font_title = 90
        font_subtitle = 50
        font_restart_button = 30

        # タイトル
        self.title_label = None
        self.subtitle_label = None
        self.title_label = tk.Label(self, text=self.title, font=("Arial", font_title, 'bold'), bg="white")
        self.title_label.pack(pady=(300, 100))

        # サブタイトル
        self.subtitle_label = tk.Label(self, text=self.subtitle, font=("Arial", font_subtitle, 'bold'), bg="white")
        self.subtitle_label.pack(pady=5)

        # スタート画面に戻る
        self.restart_button = tk.Button(self, text=self.restart_button_text, font=("Arial", font_restart_button, 'bold'), command=self.restart, fg='white', bg='red')
        self.restart_button.pack(pady=50)

    def restart(self):
        """
        スタート画面に戻る
        """
        self.pomo_timer.rep.rep_now = 0
        self.master.show_start_window()


if __name__ == "__main__":
    pass


