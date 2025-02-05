import time
class Timer(object):
    total_time = 0  # クラス変数として総作業時間を定義（全インスタンスで共通）
    MINUTE = 60

    def __init__(self, time: int):
        """
            時間の抽象化クラス
        Args:
            times ( int ): minutes(分)
        """
        self.set_time = time
        self.currnet_time = self.Minute2Second(self.set_time)

    def CountDown(self):
        """
            秒数を1秒ずつ減らす
        """
        self.currnet_time -= 1
        time.sleep(1.0)

    def ResetTime(self):
        """
            秒数を初期化
        """
        self.currnet_time = self.Minute2Second(self.set_time)

    def Minute2Second(self, m):
        """
            分を秒に変換
        Args:
            m ( int ): minute(分)

        Returns:
            int : 秒を返す
        """
        sec = m * self.MINUTE
        return sec
    
    def Transform(self):
        """
            秒を分と秒に変換
        Args:
            sec ( int ): second(秒)
        """
        m = self.currnet_time // self.MINUTE
        s = self.currnet_time % self.MINUTE

        return m, s
    
    @classmethod
    def set_total_time(cls, total_time):
        cls.total_time = total_time


class TimeWork(Timer):
    def __init__(self, work_time: int):
        """
            作業クラス
        Args:
            times ( int ): minutes(分)
        """
        super().__init__(work_time)
        self.seconds = self.Minute2Second(work_time)

class TimeRest(Timer):
    def __init__(self, rest_time: int):
        """
            休憩クラス
        Args:
            times ( int ): minutes(分)
        """
        super().__init__(rest_time)
        self.seconds = self.Minute2Second(rest_time)


if __name__ == "__main__":
    work = TimeWork(work_time=50)
    Timer.set_total_time(120)
    print(work.total_time)

