"""
タプル「sports」があります。for文と「enumerate」を利用して、
以下のように表示する処理を作成してください

0 --> 野球
1 --> サッカー
2 --> テニス
3 --> ダンス
"""

sports = ("野球","サッカー","テニス","ダンス")

for i, v in enumerate(sports):
    print( str(i) + " --> " + v)

