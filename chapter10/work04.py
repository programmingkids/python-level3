"""
リスト「data」があります。リストコンプリヘンションを利用して、
リスト「data」から「4の倍数」のみのリストを作成してください

以下のように表示する処理を作成してください

[4, 8, 12]
"""

data = [4,3,6,8,12,7,10,2]

data = [i for i in data if i % 4 == 0]
print(data)
