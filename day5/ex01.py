# set n=5 as the example
board_condition = [[0]*5 for i in range(5)]
# board_condition

list_user = [[0]*5 for i in range(5)]
list_enemy = [[0]*5 for i in range(5)]

# print the chess board
def chess_print():
    for i in range((5-1)*2+1):
        for j in range((5-1)*3+1):
            if(i%2 == 0):
                if (j%3 == 0):
                    if(board_condition[int(i/2)][int(j/3)] == 0):
                        print('+',end="")
                    elif(board_condition[int(i/2)][int(j/3)] == 1):
                        print('M',end="")
                    elif(board_condition[int(i/2)][int(j/3)] == 2):
                        print('X',end="")
                    elif(board_condition[int(i/2)][int(j/3)] == 3):
                        print('S',end="")
                else:
                    print('-',end="")
            else:
                if (j%3 == 0):
                    print('|',end="")
                else:
                    print(' ',end="")
        print()


# change the board condition
def input_change():
    if temp[2].upper() == 'M':
        board_condition[int(temp[0])-1][int(temp[1])-1] = 1
    elif temp[2].upper() == 'X':
        board_condition[int(temp[0])-1][int(temp[1])-1] = 2
    elif temp[2].upper() == 'S':
        board_condition[int(temp[0])-1][int(temp[1])-1] = 3

# 设置更改自己的状态函数
def change_state(list):
    list[int(temp[0])-1][int(temp[1])-1] = 1

# 改变对手的棋盘状况
# 基于n=5的情况
def opposite_state(list):
    list[int(temp[0])-1][int(temp[1])-1] = 1
    if temp[2].upper() == 'M':
        # 加上检测条件
        if (int(temp[0])-1+1) in range (0,5) and (int(temp[1])-1+2) in range(0,5):
            list[int(temp[0])-1+1][int(temp[1])-1+2] = 1
        if (int(temp[0])-1+1) in range (0,5) and (int(temp[1])-1-2) in range(0,5):
            list[int(temp[0])-1+1][int(temp[1])-1-2] = 1
        if (int(temp[0])-1-1) in range (0,5) and (int(temp[1])-1+2) in range(0,5):
            list[int(temp[0])-1-1][int(temp[1])-1+2] = 1
        if (int(temp[0])-1-1) in range (0,5) and (int(temp[1])-1-2) in range(0,5):
            list[int(temp[0])-1-1][int(temp[1])-1-2] = 1
        if (int(temp[0])-1+2) in range (0,5) and (int(temp[1])-1+1) in range(0,5):
            list[int(temp[0])-1+2][int(temp[1])-1+1] = 1
        if (int(temp[0])-1+2) in range (0,5) and (int(temp[1])-1-1) in range(0,5):
            list[int(temp[0])-1+2][int(temp[1])-1-1] = 1
        if (int(temp[0])-1-2) in range (0,5) and (int(temp[1])-1+1) in range(0,5):
            list[int(temp[0])-1-2][int(temp[1])-1+1] = 1
        if (int(temp[0])-1-2) in range (0,5) and (int(temp[1])-1-1) in range(0,5):
            list[int(temp[0])-1-2][int(temp[1])-1-1] = 1
    elif temp[2].upper() == 'X':
        if (int(temp[0])-1+2) in range (0,5) and (int(temp[1])-1+2) in range(0,5):
            list[int(temp[0])-1+2][int(temp[1])-1+2] = 1
        if (int(temp[0])-1+2) in range (0,5) and (int(temp[1])-1-2) in range(0,5):
            list[int(temp[0])-1+2][int(temp[1])-1-2] = 1
        if (int(temp[0])-1-2) in range (0,5) and (int(temp[1])-1+2) in range(0,5):
            list[int(temp[0])-1-2][int(temp[1])-1+2] = 1
        if (int(temp[0])-1-2) in range (0,5) and (int(temp[1])-1-2) in range(0,5):
            list[int(temp[0])-1-2][int(temp[1])-1-2] = 1
    elif temp[2].upper() == 'S':
        if (int(temp[0])-1+1) in range (0,5) and (int(temp[1])-1+1) in range(0,5):
            list[int(temp[0])-1+1][int(temp[1])-1+1] = 1
        if (int(temp[0])-1+1) in range (0,5) and (int(temp[1])-1-1) in range(0,5):
            list[int(temp[0])-1+1][int(temp[1])-1-1] = 1
        if (int(temp[0])-1-1) in range (0,5) and (int(temp[1])-1+1) in range(0,5):
            list[int(temp[0])-1-1][int(temp[1])-1+1] = 1
        if (int(temp[0])-1-1) in range (0,5) and (int(temp[1])-1-1) in range(0,5):  
            list[int(temp[0])-1-1][int(temp[1])-1-1] = 1

# 检测函数，判断能不能下这一步棋
def exam(list):
    if(list[int(temp[0])-1][int(temp[1])-1] == 1):
        print("It is the enemy domain, please choose another place")
        return 1

# 判断输赢函数
def win_or_lose_judgement(list):
    consequence = 1
    for i in range(5):
        for j in range(5):
            if(list[i][j] == 0):
                consequence = 0
    return consequence


# for machine
# 全部下马
# 周围八个顶点都检测一遍，如果不行，那就从头开始遍历，找到第一个可以落子的点
def machine_moving():
    while True:
        if (int(temp[1])-1+1) in range(5): 
            if list_enemy[int(temp[0])-1][int(temp[1])-1+1] == 0:
                temp[1] = str(int(temp[1])+1)
                temp[2] = 'm'
                break

        elif (int(temp[1])-1-1) in range(5):
            if list_enemy[int(temp[0])-1][int(temp[1])-1-1] == 0:
                temp[1] = str(int(temp[1])-1)
                temp[2] = 'm'
                break

        elif (int(temp[0])-1-1) in range(5):
            if list_enemy[int(temp[0])-1-1][int(temp[1])-1] == 0:
                temp[0] = str(int(temp[0])-1)
                temp[2] = 'm'
                break

        elif (int(temp[0])-1+1) in range(5):
            if list_enemy[int(temp[0])-1+1][int(temp[1])-1] == 0:
                temp[0] = str(int(temp[0])+1)
                temp[2] = 'm'
                break

        elif (int(temp[1])-1+1) in range(5) and (int(temp[0])-1-1) in range(5):
            if list_enemy[int(temp[0])-1-1][int(temp[1])-1+1] == 0:
                temp[0] = str(int(temp[0])-1)
                temp[1] = str(int(temp[1])+1)
                temp[2] = 'm'
                break


        elif (int(temp[1])-1-1) in range(5) and (int(temp[0])-1-1) in range(5):
            if list_enemy[int(temp[0])-1-1][int(temp[1])-1-1] == 0:
                temp[0] = str(int(temp[0])-1)
                temp[1] = str(int(temp[1])-1)
                temp[2] = 'm'
                break
                

        elif (int(temp[1])-1+1) in range(5) and (int(temp[0])-1+1) in range(5):
            if list_enemy[int(temp[0])-1+1][int(temp[1])-1+1] == 0:
                temp[0] = str(int(temp[0])+1)
                temp[1] = str(int(temp[1])+1)
                temp[2] = 'm'
                break

        elif (int(temp[1])-1-1) in range(5) and (int(temp[0])-1+1) in range(5):
            if list_enemy[int(temp[0])-1+1][int(temp[1])-1-1] == 0:
                temp[0] = str(int(temp[0])+1)
                temp[1] = str(int(temp[1])-1)
                temp[2] = 'm'
                break

        else:
        #     遍历整个数组
            for i in range(5):
                for j in range (5):
                    if(list_enemy[i][j] == 0):
        #                 就在这里落子
                        list_enemy[i][j] = 1
                        temp[0] = str(i+1)
                        temp[1] = str(j+1)
                        temp[2] = 'm'
                        break

chess_print()

str_input = input('Input your choice, the place and the type:(i,j,C) ')
temp = str_input.split(',')
input_change()
chess_print()
change_state(list_user)
opposite_state(list_enemy)



while True:
    # test machine
    print('enemy')
    print(list_enemy)

    if(win_or_lose_judgement(list_enemy) == 1):
        print('user win')
        break


    machine_moving()
    input_change()
    chess_print()
    change_state(list_enemy)
    opposite_state(list_user)
    if(win_or_lose_judgement(list_enemy) == 1):
        print('enemy win')
        break


    # test user
    print('user')
    print(list_user)

    if(win_or_lose_judgement(list_user) == 1):
        print('enemy win')
        break


    str_input = input('Input your choice, the place and the type:(i,j,C) ')
    temp = str_input.split(',')
    while(exam(list_user) == 1):
        str_input = input('Input your choice, the place and the type:(i,j,C) ')
        temp = str_input.split(',')
    input_change()
    chess_print()
    change_state(list_user)
    opposite_state(list_enemy)
    if(win_or_lose_judgement(list_user) == 1):
        print('user win')
        break

        



