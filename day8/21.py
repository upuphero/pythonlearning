list1 = [1,2,3,4,5]

def printarray(b):
    for a in b:
        print(a,end = ' ')
    return a

def reversarray(c):
    for num1 in reversed(c) :
        print ( num1 , end = ' ' )
    return num1

printarray(list1)
print('\n')
reversarray(list1)
