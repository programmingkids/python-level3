"""
リスト「data」があります。map関数とラムダ関数を利用して、
リスト「data」の要素を「3倍」にした、新しいリストを作成してください

以下のように表示する処理を作成してください

[6, 9, 21, 12, 24]
"""

data = [2,3,7,4,8]

result = list(map(lambda n : n * 3, data))
print(result)