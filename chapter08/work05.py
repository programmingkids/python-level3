# クラス定義
class Character:
    money = 0
    
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print("I am " + self.name)
        print("Money is " + str(Character.money))
    
    @classmethod
    def add_money(cls, money):
        cls.money += money

    @classmethod
    def get_money(cls):
        return cls.money


# インスタンス作成
c1 = Character("John")
c2 = Character("Bob")

# クラスメソッド呼び出し
Character.add_money(10)
Character.add_money(20)
Character.add_money(30)

# クラスメソッド呼び出し
print("クラスメソッド")
money = Character.get_money()
print("Money is " + str(money))

# インスタンスメソッドで確認
print("インスタンスメソッド")
c1.show()
c2.show()
