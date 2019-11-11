a = ['ye','li','wang','liu']
print(a)
a += ['zhao','qian'] #在最后加上
print(a)

b = a[1:4]  #切割list，保留第二个，第三个，第四个
print(b)

c = a[:]
print('c=',c)