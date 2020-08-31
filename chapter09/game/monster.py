# 複数のクラスを定義するモジュール
class Enemy :
    def __init__(self, name, attackPoint):
        self.name = name
        self.attackPoint = attackPoint


class Dragon (Enemy) :
    def attack(self):
        print(self.name + "は炎で攻撃した")
        print("攻撃力は「" + str(self.attackPoint) + "」でした")


class Slime (Enemy) :
    def attack(self):
        print(self.name + "は体当たりで攻撃した")
        print("攻撃力は「" + str(self.attackPoint) + "」でした")

