c = [1,2,4,56,78]
print('c=', c) 
# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
c.pop(0) #删除第一个
print(c)
c.pop(len(c) - 1) #删除最后一个
print(c) # 
c.clear()
print(c) #删到只剩[]

