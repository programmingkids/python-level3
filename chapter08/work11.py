"""
クラス「Enemy」を継承したクラス「Dragon」を作成してください
クラス「Enemy」を継承したクラス「DarkKnight」を作成してください

以下のように表示する処理を作成してください

敵：ファイヤードラゴンが現れた
ファイヤードラゴンによる巨大な炎の攻撃
20のダメージを与えた
====
敵：悪魔の騎士が現れた
悪魔の騎士によるイナズマの攻撃
25のダメージを与え
"""

class Enemy:
    def __init__(self, name, attackPoint):
        self.name = name
        self.attackPoint = attackPoint

    def show(self):
        print("敵：" + self.name + "が現れた")
        
    def attack(self):
        pass


# 以下の部分にクラスを定義します
class Dragon (Enemy) :
    def attack(self):
        print(self.name + "による巨大な炎の攻撃")
        print(str(self.attackPoint) + "のダメージを与えた")
        

class DrakKnight (Enemy) :
    def attack(self):
        print(self.name + "によるイナズマの攻撃")
        print(str(self.attackPoint) + "のダメージを与えた")
    

# 以下の部分は修正してはいけません
dragon = Dragon("ファイヤードラゴン", 20)
dragon.show()
dragon.attack()

print("====")

darkKnight = DrakKnight("悪魔の騎士", 25)
darkKnight.show()
darkKnight.attack()
