# 関数定義
def show_foods(*foods):
    for f in foods:
        print("私の好きな食べ物は「" + f + "」です")


# 関数呼び出し
show_foods("寿司","ピザ","カレー","唐揚げ")
