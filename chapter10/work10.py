"""
クラス「Singer」を継承したクラス「Idol」を作成してください

以下のように表示する処理を作成してください

乃木坂46はアイドルです
楽しく歌っておどります
====
AKB48はアイドルです
楽しく歌っておどります
"""

class Singer:
    def __init__(self, name):
        self.name = name
    
    def sing(self):
        print("歌を歌います")


# 以下の部分にクラスを定義します
class Idol (Singer):
    def sing(self):
        print(self.name + "はアイドルです")
        print("楽しく歌っておどります")


# 以下の部分は修正してはいけません
idol1 = Idol("乃木坂46")
idol1.sing()

print("====")

idol2 = Idol("AKB48")
idol2.sing()
