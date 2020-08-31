# 親クラス定義
class Monster:
    def __init__(self, name, attackPoint):
        self.name = name
        self.attackPoint = attackPoint
    
    def show(self):
        print(self.name + "は攻撃した")


# 子クラス定義    
class Dragon (Monster):
    def __init__(self, name, attackPoint, weapon):
        super().__init__(name, attackPoint)
        self.weapon = weapon
    
    def attack(self):
        print("[" + self.weapon + "] による攻撃")
        print("[" + str(self.attackPoint) + "] のダメージを与えた")


# インスタンス作成
d1 = Dragon("炎の竜", 15, "巨大なマグマ")
d1.show()
d1.attack()

print("====")

# インスタンス作成
d2 = Dragon("氷の竜", 20, "アイストルネード")
d2.show()
d2.attack()
