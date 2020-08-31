"""
リスト「numbers」があります。リストコンプリヘンションを利用して、
リスト「numbers」から「3の倍数」のみのリストを作成してください

以下のように表示する処理を作成してください

[3, 6, 9]
"""

numbers = [4,3,6,2,9,5]

numbers = [x for x in numbers if x % 3 == 0]
print(numbers)
