a = [1,3,56,79,245]
a.append(2678)  # append() 方法用于在列表末尾添加新的对象。

print(a) # [1, 3, 56, 79, 245, 2678]
print(len(a))
a.insert(4,123) #前面的4是在list中第几个元素的意思，在第四个后加123

print(a)  #[1, 3, 56, 79, 123, 245, 2678]
a += [1000, 2000] #也是在list最后加上
print(a)  #[1, 3, 56, 79, 123, 245, 2678, 1000, 2000]
print(len(a))


b = [1,2,4,56,78]
print('b=', b)
if 3 in b:
    b.remove(3)
if 4 in b:
    b.remove(56)
print(b)
