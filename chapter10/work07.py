"""
「colors1」と「colors2」の2個のセットがあります。
「union」を利用して、2個のセットの「和」を作成してください

実行結果のように表示する処理を作成してください

{'Red', 'Blue', 'Purple', 'Green', 'Pink'}
"""

colors1 = {"Red","Blue","Pink"}
colors2 = {"Green","Pink","Red", "Purple"}

print(colors1.union(colors2))
