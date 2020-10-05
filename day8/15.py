dict1 = {'name':'两点水','age':'23','sex':'男'}

for key in dict1 :    # 迭代 dict 中的 key
    print ( key , end = ' ' )

print('\n')

for value in dict1.values() :   # 迭代 dict 中的 value
	print ( value , end = ' ' )

print ('\n')

# 如果 list 里面一个元素有两个变量，也是很容易迭代的
for x , y in [ (1,'a') , (2,'b') , (3,'c') ] :
	print ( x , y )