"""
クラス「Character」を継承したクラス「Hero」を作成してください
クラス「Character」を継承したクラス「Magician」を作成してください

以下のように表示する処理を作成してください

ミッキーのHPは「20」
ミッキーの攻撃
勇者は勇敢に戦った
====
ミニーのHPは「35」
ミニーの攻撃
魔法使いは魔法で戦った
"""

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
    def show(self):
        print(self.name + "のHPは「" + str(self.hp) + "」")


# 以下の部分にクラスを定義します





# 以下の部分は修正してはいけません
hero = Hero("ミッキー", 20)
hero.show()
hero.attack()

print("====")

magician = Magician("ミニー", 35)
magician.show()
magician.attack()
