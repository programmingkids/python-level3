"""
関数「get_triangle_area」を定義してください

関数名：get_triangle_area
引数：2個　base（底辺）、height（高さ）
戻り値：数値
処理：2個の引数（底辺と高さ）に基づいて三角形の面積を計算します。
三角形の面積を戻り値として返します

以下のように表示する処理を作成してください

10.0
"""

# 以下の部分に関数を定義します
def get_triangle_area(base, height):
    area = (base * height) / 2
    return area


# これ以降は修正してはいけません
num1 = 4
num2 = 5
print(get_triangle_area(num1, num2))
