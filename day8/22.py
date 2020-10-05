class A():
    a=1
    b=2
    c=3
    def fun1():
        print('function1')
        return 'func1'
    def fun2():
        print('function2')
    def fun3():
        print('function3')

print(A.a)
b=A.fun1()
print(b)
A.fun3()
A.fun2()
