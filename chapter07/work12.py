"""
関数「show_members」を定義してください

関数名：show_members
引数：1個（可変長引数をタプルで受け取る）
戻り値：なし
処理：可変長引数で受け取ったタプルの要素をfor文を利用して表示します

以下のように表示する処理を作成してください

John
Bob
Tom
Scot
"""

# 以下の部分に関数を定義します
def show_members(*members):
    for member in members:
        print(member)


# これ以降は修正してはいけません
show_members("John","Bob","Tom","Scot")
