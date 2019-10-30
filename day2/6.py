"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...
Version: 1.0
Date: 2019-10-30
"""
a = 0
b = 1
sum=0
for _ in range(20):
    sum=a+b
    a=b
    b=sum
    
    print(a,end=' ')
print('The end')
'''
a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')
'''