# クラス定義
class Player:
    def show_name(self):
        print("I am " + self.name)
    
    def show_age(self):
        print("I am " + str(self.age) + " years old")


# インスタンス作成
player1 = Player()
player1.name = "Micky"
player1.age = 17
player1.show_name()
player1.show_age()

print("====")

# インスタンス作成
player2 = Player()
player2.name = "Minny"
player2.age = 16
player2.show_name()
player2.show_age()
