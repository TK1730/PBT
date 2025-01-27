import tkinter as tk
import random

from Timer import timer

class GUI(object):
    def __init__(self):
        # 初期設定
        self.phase = True  # 作業: True 休憩 False
        self.current_session = 0  # 繰り返し回数

        # ウィンドウの作成
        self.root = tk.Tk()
        self.root.title("Pomodoro Blackout Timer")
        self.root.geometry("500x500")

        # ラベルを作成
        self.label = tk.Label(self.root, text="Push the Button", font=("Arial", 30))
        self.label.pack()

        # ボタンを作成
        self.button = tk.Button(self.root, command=self.on_button_click, text="25min", font=("Arial", 30))
        self.button.pack()

        # カウントダウンのラベル
        self.countdown_label = tk.Label(self.root, text="3", font=("Arial", 40), fg="black", bg="white")  # 秒数を表示→3から
        self.left_time = 10

    def countdown(self):
        """カウントダウンを更新する処理"""
        if self.left_time > 0:
            self.countdown_label.config(text=str(self.left_time))  # ラベルにカウントダウンの数字を表示
            self.left_time -= 1
            self.root.after(1000, self.countdown)  # 1秒ごとにカウントダウン
        else:
            self.turn_dark()  # 残り時間が0になったらウィンドウを真っ暗にし、ボタンを削除

    def on_button_click(self):
        """ボタンがクリックされたときの処理"""
        self.label.config(text="GO FOR IT!!!!!!!!!!", font=("Arial", 30))  # ラベルのテキストを変更
        self.countdown_label.pack(pady=50)  # カウントダウンラベルを表示
        self.countdown()  # 1秒ごとにカウントダウンを更新

    def turn_dark(self):
        """ウィンドウを真っ暗にする処理"""
        rest_option = ['仮眠', '食事', 'つむつむ']
        self.root.configure(bg='black')  # ウィンドウの背景色を黒に設定
        self.label.config(text=random.choice(rest_option), font=("Arial", 30), fg="white", bg="black")  # ラベルを更新して休憩方法を表示
        self.button.destroy()
        self.countdown_label.destroy()

if __name__ == "__main__":
    gui = GUI()
    gui.root.mainloop()
print('brach change')

