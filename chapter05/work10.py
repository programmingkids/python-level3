"""
ディクショナリ「characters」があります。for文と「keys()」を利用して
以下のように表示する処理を作成してください

Micky
Donald
Ariel
Bell
"""

characters = {
    "Micky" : "魔法使い",
    "Donald" : "戦士",
    "Ariel" : "武闘家",
    "Bell" : "賢者",
}

for name in characters.keys():
    print(name)
