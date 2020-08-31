# Characterクラスを定義するモジュール
class Character:
    def __init__(self, name, level, job):
        self.name = name
        self.level = level
        self.job = job
    
    def show(self):
        print("I am " + self.name)
        print("My level is " + str(self.level))
        print("My job is " + self.job)

