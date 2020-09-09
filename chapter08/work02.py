# クラス定義
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_name(self):
        print("I am " + self.name)
    
    def show_age(self):
        print("I am " + str(self.age) + " years old")


# インスタンス作成
player1 = Player("Micky", 17)
player1.show_name()
player1.show_age()

print("====")

# インスタンス作成
player2 = Player("Minny", 16)
player2.show_name()
player2.show_age()
