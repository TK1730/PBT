import time
class Timer(object):
    def __init__(self, times):
        """
            時間の抽象化クラス
        Args:
            times ( int ): minutes(分)
        """
        # 分
        self.times = times
        #　秒
        self.seconds = self.Minute2Second(self.times)

        self.minutes = 60

    def CountDown(self):
        """
            秒数を1秒ずつ減らす
        """
        self.seconds -= 1
        time.sleep(1.0)

    def ResetTime(self):
        """
            秒数を初期化
        """
        self.seconds = self.Minute2Second(self.times)

    def Minute2Second(self, m):
        """
            分を秒に変換
        Args:
            m ( int ): minute(分)

        Returns:
            int : 秒を返す
        """
        sec = m * self.minutes
        return sec
    
    def Transfoemer(self):
        """
            秒を分と秒に変換
        Args:
            sec ( int ): second(秒)
        """
        m = self.seconds // self.minutes
        s = self.seconds % self.minutes

        return m, s


class TimeWork(Timer):
    def __init__(self, times):
        """
            作業クラス
        Args:
            times ( int ): minutes(分)
        """
        super().__init__(times)


class TimeRest(Timer):
    def __init__(self, times):
        """
            休憩クラス
        Args:
            times ( int ): minutes(分)
        """
        super().__init__(times)

    
if __name__ == "__main__":
    t = TimeWork(25)
    for i in range(10):
        t.CountDown()
        print(t.seconds)
