"""
ディクショナリ「characters」があります。for文と「items()」を利用して
以下のように表示する処理を作成してください

Micky (魔法使い)
Donald (戦士)
Ariel (武闘家)
Bell (賢者)
"""

characters = {
    "Micky" : "魔法使い",
    "Donald" : "戦士",
    "Ariel" : "武闘家",
    "Bell" : "賢者",
}

for key, value in characters.items():
    print(key + " (" + value + ")")
