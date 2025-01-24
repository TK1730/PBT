import tkinter as tk
import random
from itertools import count

if __name__ == '__main__':

    # カウントダウンを更新する処理　→　ここを書き直して　主に
    def update_countdown(counter, label):
        if counter > 0:
            label.config(text=str(counter))  # ラベルにカウントダウンの数字を表示
            root.after(1000, update_countdown, counter - 1, label)  # 1秒ごとにカウントダウン
        else:
            turn_dark(label)  # 3秒後にウィンドウを真っ暗にし、ボタンを削除

    # ボタンがクリックされたときの処理
    def on_button_click():
        label.config(text="GO FOR IT!!!!!!!!!!", font=("Arial", 30))  # ラベルのテキストを変更
        global countdown_label
        countdown_label = tk.Label(root, text="3", font=("Arial", 40), fg="black", bg="white")  # 秒数を表示→3から
        countdown_label.pack(pady=50)  # カウントダウンラベルを表示
        update_countdown(3, countdown_label)  # 1秒ごとにカウントダウンを更新　3から表示スタート


    # ウィンドウが真っ暗になる処理
    def turn_dark(countdown_label):
        rest_option = ['仮眠', '食事', 'つむつむ']
        root.configure(bg='black')  # ウィンドウの背景色を黒に設定
        label.config(text=random.choice(rest_option), font=("Arial", 30), fg="white", bg="black")  # ラベルを更新して休憩方法を表示
        button.destroy()
        countdown_label.destroy()

    # ウィンドウの作成
    root = tk.Tk()
    root.title("Pomodoro Blackout Timer")
    root.geometry("500x500")

    # ラベルを作成
    label = tk.Label(root, text="Push the Button", font=("Arial", 30))
    label.pack()

    # ボタンを作成
    button = tk.Button(root, command=on_button_click, text="25min", font=("Arial", 30))
    button.pack()

    # イベントループを開始
    root.mainloop()

print('brach change')

