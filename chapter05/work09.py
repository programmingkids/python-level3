"""
ディクショナリ「data1」と「data2」があります。2個のディクショナリを
1個のディクショナリに結合してください

以下のように表示する処理を作成してください

{'東京': 88, '神奈川': 93, '千葉': 90, '大阪': 91, '京都': 85}
"""

data1 = {
    "東京" : 88,
    "神奈川" : 93,
    "千葉" : 90,
}

data2 = {
    "大阪" : 91,
    "京都" : 85,
}

data1.update(data2)
print(data1)
