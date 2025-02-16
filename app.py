from utils import GUI, pomodotimer

def main():
    pomo = pomodotimer.PomodoroTimer(1, 1)
    app = GUI.PomodoroWindow(pomo)
    app.mainloop()

if __name__ == '__main__':
    main()