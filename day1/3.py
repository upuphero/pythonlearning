year=int(input('The year is '))
leap = (year%4==0 and year%100!=0)or year%400==0

print(leap)

