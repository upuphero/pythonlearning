a = [1,2,3,4,45,64,123,156]

b=['hello']
c=b*3
print(a)
'''
print(c)
print(b)
print(len(a))
print(len(b)) #计算元素个数
print(len(c))
print(a[3])
print(c[2])

a[2]=200
print(a)
print(a[2])
for index in range(len(a)):
    print(a[index])
'''
'''
for elem in a:
    print(elem)
    elem-=1
    print(elem)
'''   
for index, elem in enumerate(a):
    print(index, elem)