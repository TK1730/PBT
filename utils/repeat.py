class Repeat(object):
    def __init__(self, hours):
        self.rep_limit = hours * 2
        self.rep_now = 0
        self.flag_finish = False

    def repeat_count(self):
        """
            繰り返し回数をカウント
        """
        self.rep_now += 1

    def completion_judg(self):
        """
            繰り返し回数に達したか判定
        """
        if self.rep_limit == self.rep_now:
            self.flag_finish = True


if __name__ == '__main__':
    repe = Repeat(4)
    print(repe.flag_finish)
    for i in range(10):
        print(i)
        repe.repeat_count()
        repe.completion_judg()
        if repe.flag_finish:
            break
    print("finish")
