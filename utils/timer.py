import time
class Timer(object):
<<<<<<< HEAD
    def __init__(self, times):
=======
    total_time = 0  # クラス変数として総作業時間を定義（全インスタンスで共通）
    MINUTE = 60

    def __init__(self, time: int):
>>>>>>> feature-app
        """
            時間の抽象化クラス
        Args:
            times ( int ): minutes(分)
        """
<<<<<<< HEAD
        # 分
        self.times = times
        #　秒
        self.seconds = self.Minute2Second(self.times)

        self.minutes = 60
=======
        self.time = time
        self.seconds = self.Minute2Second(time)
>>>>>>> feature-app

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
<<<<<<< HEAD
        sec = m * self.minutes
        return sec
    
    def Transfoemer(self):
=======
        sec = m * self.MINUTE
        return sec
    
    def Transform(self):
>>>>>>> feature-app
        """
            秒を分と秒に変換
        Args:
            sec ( int ): second(秒)
        """
<<<<<<< HEAD
        m = self.seconds // self.minutes
        s = self.seconds % self.minutes

        return m, s


class TimeWork(Timer):
    def __init__(self, times):
=======
        m = self.seconds // self.MINUTE
        s = self.seconds % self.MINUTE

        return m, s
    
    @classmethod
    def set_total_time(cls, total_time):
        cls.total_time = total_time


class TimeWork(Timer):
    def __init__(self, work_time: int):
>>>>>>> feature-app
        """
            作業クラス
        Args:
            times ( int ): minutes(分)
        """
<<<<<<< HEAD
        super().__init__(times)


class TimeRest(Timer):
    def __init__(self, times):
=======
        super().__init__(work_time)
        self.seconds = self.Minute2Second(work_time)

class TimeRest(Timer):
    def __init__(self, rest_time: int):
>>>>>>> feature-app
        """
            休憩クラス
        Args:
            times ( int ): minutes(分)
        """
<<<<<<< HEAD
        super().__init__(times)

    
if __name__ == "__main__":
    t = TimeWork(25)
    for i in range(10):
        t.CountDown()
        print(t.seconds)
=======
        super().__init__(rest_time)
        self.seconds = self.Minute2Second(rest_time)


if __name__ == "__main__":
    work = TimeWork(work_time=50)
    Timer.set_total_time(120)
    print(work.total_time)

>>>>>>> feature-app
