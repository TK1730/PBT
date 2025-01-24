import time

class timer(object):
    def __init__(self, total_time):
        self.total_time = total_time  # 総作業時間 : 時間
        self.work_time = 25  # 作業時間 : 分
        self.rest_time = 5  # 休憩時間 : 分
        self.work_sec_time = self.minu2sec(self.work_time)  # 作業時間 : 秒
        self.rest_sec_time = self.minu2sec(self.rest_time)  # 作業時間 : 秒

    def count_down_work(self):
        # 作業時間のカウントダウン
        self.work_sec_time -= 1  
    
    def cout_down_rest(self):
        # 休憩時間のカウントダウン
        self.rest_time -= 1

    def minu2sec(self, minutes):
        return int(minutes * 60)
    
    
    def repeat_calc(self, total_time):
        return total_time // (self.work_time + self.rest_time)
    
    def reset_time(self):
        self.work_sec_time = self.minu2sec(self.work_time)
        self.rest_sec_time = self.minu2sec(self.rest_time)

if __name__ == "__main__":
    t = timer(1)

