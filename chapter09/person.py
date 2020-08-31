# Personクラスを定義するモジュール
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print("I am " + self.name)
        print("I am " + str(self.age) + " years old")

