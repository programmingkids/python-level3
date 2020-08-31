# クラス定義
class Person:
    def show_name(self):
        print("I am " + self.name)
    
    def show_age(self):
        print("I am " + str(self.age) + " years old")


# インスタンス作成
p1 = Person()
p1.name = "Micky"
p1.age = 17
p1.show_name()
p1.show_age()

print("====")

# インスタンス作成
p2 = Person()
p2.name = "Minny"
p2.age = 16
p2.show_name()
p2.show_age()
