"""
ディクショナリ「nations1」と「nations2」があります。2個のディクショナリを
1個のディクショナリに結合してください

以下のように表示する処理を作成してください

{'Japan': 'Tokyo', 'England': 'London', 'France': 'Paris', 'Spain': 'Madrid', 'Italy': 'Roma'}
"""

nations1 = {
    "Japan" : "Tokyo",
    "England" : "London",
}

nations2 = {
    "France" : "Paris",
    "Spain" : "Madrid",
    "Italy" : "Roma",
}

nations1.update(nations2)
print(nations1)
