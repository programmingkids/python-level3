# クラス定義
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def get_triangle_area(self):
        area = (self.base * self.height) / 2
        return area


# インスタンス作成
t1 = Triangle(10, 5)
result = t1.get_triangle_area()
print(result)
