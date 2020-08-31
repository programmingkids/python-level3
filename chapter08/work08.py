# 親クラス定義
class Car:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print("車の名前：" + self.name)
        
    def move(self):
        print("ガソリンで車が動作します")
        

# 子クラス定義
class HybridCar (Car):
    def move(self):
        print("ハイブリッドで車が動作します")


# 子クラス定義
class ElectricCar (Car):
    def move(self):
        print("電気で車が動作します")


# インスタンス作成
car1 = HybridCar("プリウス")
car1.show()
car1.move()

print("===")

# インスタンス作成
car2 = ElectricCar("ノート")
car2.show()
car2.move()
