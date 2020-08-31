"""
for文とif文を利用して、リスト「members」から「Elsa」と「Anna」のみを
以下のように表示する処理を作成してください

Elsa
Anna
"""

members = ["Micky","Minny","Elsa","Donald","Anna"]

for member in members:
    if member == "Elsa" or member == "Anna":
        print(member)

