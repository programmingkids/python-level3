# クラス定義
class Character:
    money = 0
    
    def __init__(self, name, job , hp):
        self.name = name
        self.job = job
        self.hp = hp
        
    def show(self):
        print("私は" + self.name)
        print("私の職業は" + self.job)
        print("私のHPは" + str(self.hp))
        print("所持金は" + str(Character.money))
    

# クラス変数に代入
Character.money = 100

# インスタンス作成
c1 = Character("ミッキー", "勇者",20)
c1.show()

print("====")

# インスタンス作成
c2 = Character("ミニー", "魔法使い", 10)
c2.show()
