# 関数定義
def show_myself(**data):
    print("I am " + data["name"] )
    print("I am " + str(data["age"]) + " years old")
    print("My hobby is " + data["hobby"])


# 関数呼び出し
show_myself(name="Minny", age=17, hobby="cooking")
