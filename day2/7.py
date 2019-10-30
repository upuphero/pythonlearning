'''判断素数'''
import math
c = int(input("请输入一个整数(>1)："))
k = int(math.sqrt(c))
for i in range(2, k+2):
  if c % i == 0:
    break #可以整除，肯定不是素数，结束循环
if i == k+1: print(c, "是素数！")
else: print(c, "是合数！")