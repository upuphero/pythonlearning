count = 0
sum = 0
while (count < 100):
    count = count + 1
    if ( count % 2 == 0):  # 双数时跳过输出
        continue
    sum = sum + count
print(sum)