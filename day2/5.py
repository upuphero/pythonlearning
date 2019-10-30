"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
import math

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)
"""
import math

for a in range(1,21):
    is_prime = True
    c=2**a-1
    b=2**(a-1)
    k=int(math.sqrt(c))
    for i in range(2,k+1):
        if c % i == 0:
            is_prime = False
            break
    if is_prime: 
        num=b*c
        print(num,end=' ')

