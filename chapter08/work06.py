# 親クラス定義
class Animal:
    def __init__(self, name):
        self.name = name
        
    def show_name(self):
        print("名前：" + self.name)


# 子クラス定義
class Dog (Animal):
    def cry(self):
        print("なきごえ：ワンワン")


# 子クラス定義
class Cat (Animal):
    def cry(self):
        print("なきごえ：ニャーニャー")


# インスタンス作成
dog = Dog("ポチ")
dog.show_name()
dog.cry()

print("====")

# インスタンス作成
cat = Cat("タマ")
cat.show_name()
cat.cry()
