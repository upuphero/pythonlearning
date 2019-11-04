def add(*ar):   # 在参数名前面的*表示args是一个可变参数
    total = 0
    for val in ar:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))