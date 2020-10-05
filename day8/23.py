class B():
    a=2
    b='you'

    @classmethod
    def func1(cls):
        print('fuck'+' '+cls.b)
        
    def func2(cls,age):

        print(age)
        print(cls.a)

B.func1()
B.a=input(14)
B.func2(23,5)