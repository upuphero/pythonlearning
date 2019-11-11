a = ['ye','li','wang','liu']
print(a)
a += ['zhao','qian'] #在最后加上
print('a =',a)
b = sorted(a)  #默认是首字母
print('b= ',b)
c = sorted(a, reverse=True) #reverse 就是默认排序反过来
print('c=',c)
x = ['yexi','yeretg','w','frfrfrf','2','4']
d = sorted(a, key=len)
print('d= ',d)
x = sorted(x, key=len)
print('x =',x)
a.sort(reverse=True)
print('a= ',a)
