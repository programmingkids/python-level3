"""
リスト「numbers」があります。リストコンプリヘンションを利用して、
リスト「numbers」の要素を「3倍」にしたリストを作成してください

以下のように表示する処理を作成してください

[12, 9, 18, 6, 27, 15]
"""

numbers = [4,3,6,2,9,5]

numbers = [x * 3 for x in numbers]
print(numbers)
