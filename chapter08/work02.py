# クラス定義
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_name(self):
        print("I am " + self.name)
    
    def show_age(self):
        print("I am " + str(self.age) + " years old")


# インスタンス作成
p1 = Person("Micky", 17)
p1.show_name()
p1.show_age()

print("====")

# インスタンス作成
p2 = Person("Minny", 16)
p2.show_name()
p2.show_age()
