import random
answer = random.randint(1,100)
counter=0
while True:
    counter +=1
    number = int( input('input:  '))
    if number<answer:
        print('need to be bigger')
    elif number>answer:
        print('need to be smaller')

    else:
        print('you are right')
        break
print('how many times you have guessed',counter)
if counter>5:
    print('you are fool')