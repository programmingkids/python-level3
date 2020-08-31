numbers = [3,5,6,2,9,7]

# フィルタ関数とラムダ関数の呼び出し
result = list(filter(lambda n : n % 2 != 0, numbers))
print(result)
