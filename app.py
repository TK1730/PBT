from utils import GUI, pomodotimer

def main():
    pomo = pomodotimer.PomodoroTimer()
    app = GUI.PomodoroWindow(pomo)
    app.mainloop()

if __name__ == '__main__':
    main()