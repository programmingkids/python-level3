"""
関数「show_scores」を定義してください

関数名：show_scores
引数：1個（可変長引数をディクショナリで受け取る）
戻り値：なし
処理：可変長引数で受け取ったディクショナリの要素をfor文を利用して表示します

以下のように表示する処理を作成してください

english => 90
math => 88
science => 94
history => 86
"""

# 以下の部分に関数を定義します
def show_scores(**scores):
    for key, value in scores.items():
        print(key + " => " + str(value))
    

# これ以降は修正してはいけません
show_scores(english=90, math=88, science=94, history=86)
