# クラス定義
class Character:
    money = 0
    
    def __init__(self, name):
        self.name = name
        
    def show_name(self):
        print("I am " + self.name)
    
    @classmethod
    def add_money(cls, money):
        cls.money += money

    @classmethod
    def get_money(cls):
        return cls.money


# インスタンス作成
c1 = Character("John")
c1.show_name()
c2 = Character("Bob")
c2.show_name()

# クラスメソッド呼び出し
Character.add_money(10)
Character.add_money(20)
Character.add_money(30)

# クラスメソッド呼び出し
money = Character.get_money()
print("money is " + str(money))
