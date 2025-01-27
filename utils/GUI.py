import tkinter as tk
from tkinter import messagebox

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
    スタートウィンドウに使用する変数
    """
    def __init__(self):
        super().__init__()

        self.title = "ポモドーロタイマー"
        self.subtitle = "限界を超えろ!"
        self.message = "作業時間を決めてね"
        self.start_button_text = "スタート"
        self.user_input_box = None
        self.start_button = None

    """
    スタートウィンドウが表示される
    """
    def start_window(self):
        subtitle_label = tk.Label(self.root, text=self.subtitle, font=("Arial", 16))
        subtitle_label.pack(pady=10)

        message_label = tk.Label(self.root, text=self.message, font=("Arial", 9))
        message_label.pack(pady=5)

        self.user_input_box = tk.Entry(self.root, font=("Arial", 12))
        self.user_input_box.pack(pady=5)

        self.start_button = tk.Button(self.root, text=self.start_button_text, font=("Arial", 12), command=self.receive_user_input)
        self.start_button.pack(pady=10)

        self.root.mainloop()

    """
    入力された時間を受け取る
    """
    def receive_user_input(self):
        try:
            # 入力された値を整数に変換
            self.user_input = int(self.user_input_box.get())
            print(f"入力された作業時間: {self.user_input} 時間")
        except ValueError:
            # 無効な入力があった場合
            print("有効な数値を入力してください")


class CountDownWindow(PomodoroWindow):
    """
    カウントダウンに使用する変数
    """
    def __init__(self, time_in_seconds):
        super().__init__()

        self.time_left = time_in_seconds
        self.min = 0  # 分
        self.sec = 0  # 秒

    def transformer(self):
        """
        秒数を分と秒に変換
        """
        self.min = self.time_left // 60  # 分を計算
        self.sec = self.time_left % 60  # 秒を計算

class WorkingWindow(CountDownWindow):
    """
    作業中ウィンドウに使用する変数
    """
    def __init__(self):
        super().__init__()

        self.message = ""

        self.user_input_box = None
        self.start_button = None




if __name__ == "__main__":
    window = StartWindow()
    window.start_window()


#     def receive_user_input():
#         入力された時間を受け取る
#
#
#
#
#
# class GUI(object):
#     def __init__(selfdo):
#         # 初期設定
#         self.phase = True  # 作業: True 休憩 False
#         self.current_session = 0  # 繰り返し回数
#
#         # ウィンドウの作成
#         self.root = tk.Tk()
#         self.root.title("Pomodoro Blackout Timer")
#         self.root.geometry("500x500")
#
#         # ラベルを作成
#         self.label = tk.Label(self.root, text="Push the Button", font=("Arial", 30))
#         self.label.pack()
#
#         # ボタンを作成
#         self.button = tk.Button(self.root, command=self.on_button_click, text="25min", font=("Arial", 30))
#         self.button.pack()
#
#         # カウントダウンのラベル
#         self.countdown_label_work = tk.Label(self.root, font=("Arial", 40), fg="black", bg="white")  # 作業終了10秒前カウントダウン用
#         self.countdown_label_rest = tk.Label(self.root, font=("Arial", 40), fg="black", bg="white")  # 休憩中のカウントダウンラベル用
#         self.left_time_work = 10 # 作業終了前のカウントダウン用
#         self.left_time_rest = 20 # 休憩中カウントダウン用　
#
#     def countdown_working(self):
#         """作業終了の10秒前のカウントダウンを更新する処理"""
#         if self.left_time_work:
#             self.countdown_label_work.config(text=str(self.left_time_work))  # ラベルにカウントダウンの数字を表示
#             self.left_time_work -= 1
#             self.root.after(1000, self.countdown_working)  # 1秒ごとにカウントダウン
#         else:
#             self.turn_dark()  # 残り時間が0になったらウィンドウを真っ暗にし、ボタンを削除
#
#     def countdown_rest(self):
#         """休憩中のカウントダウンを更新する処理"""
#         if self.left_time_rest:
#             self.countdown_label_rest.config(text=str(self.left_time_rest))  # ラベルにカウントダウンの数字を表示
#             self.left_time_rest -= 1
#             self.root.after(1000, self.countdown_rest)  # 1秒ごとにカウントダウン
#         else:
#             self.turn_dark()  # 残り時間が0になったらウィンドウを真っ暗にし、ボタンを削除
#
#     def on_button_click(self):
#         """ボタンがクリックされたときの処理"""
#         self.label.config(text="GO FOR IT!!!!!!!!!!", font=("Arial", 30))  # ラベルのテキストを変更
#         self.countdown_label_work.pack(pady=50)  # カウントダウンラベルを表示
#         self.countdown_working()  # 1秒ごとにカウントダウンを更新
#
#     def turn_dark(self):
#         """ウィンドウを真っ暗にする処理"""
#         rest_option = ['仮眠', '食事', 'つむつむ']
#         self.root.configure(bg='black')  # ウィンドウの背景色を黒に設定
#         self.label.config(text=random.choice(rest_option), font=("Arial", 30), fg="white", bg="black")  # ラベルを更新して休憩方法を表示
#         self.countdown_label_rest.pack(pady=50) # 休憩中カウントダウンラベルを表示
#         self.countdown_rest() # 1秒ごとにカウントダウンを更新
#         self.button.destroy()
#         self.countdown_label_work.destroy()
#


