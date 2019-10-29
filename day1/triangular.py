a=float(input('a=   '))
b=float(input('b=   '))
c=float(input('c=   '))
if a+b>c and a+c>b and b+c>a:
    print('Perimeter is ',a+b+c)
else:
    print('It is not a triangular')