"""
クラス「Book」を作成してください

以下のように表示する処理を作成してください

本名：ミッキーの冒険
金額：1200
====
本名：ミニーのお手軽レシピ
金額：1500
"""

# 以下の部分にクラスを定義します
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
    def show(self):
        print("本名：" + self.title)
        print("金額：" + str(self.price))


# 以下の部分は修正してはいけません
book1 = Book("ミッキーの冒険", 1200)
book1.show()

print("====")

book2 = Book("ミニーのお手軽レシピ", 1500)
book2.show()
