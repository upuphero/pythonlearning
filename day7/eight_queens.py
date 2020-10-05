"""
八皇后
"""
QUEEN = -1
ROAD = 0
ROWS = 8
COLS = 8

def reset(maze):
    """重置迷宫"""
    for i in range(ROWS):
        for j in range(COLS):
            maze[i][j] = ROAD 


def set_queen(maze,a=0,b=0,c=0):
    for a in range(COLS):
        for b in range(ROWS):
            maze[a][b]=QUEEN

            for c in range(b+1,ROWS):
                ''''''
                maze[c][b]= ROAD
                maze[a][c]= ROAD


def display(maze):
    """显示迷宫"""
    for row in maze:
        for col in row:
            if col == -1:
                print('■', end=' ')
            elif col == 0:
                print('□', end=' ')
            else:
                print(f'{col}'.ljust(2), end='')
        print()


def main():
    """主函数"""
    maze = [[0] * COLS for _ in range(ROWS)]
    reset(maze)
    set_queen(maze)
    display(maze)


if __name__ == '__main__':
    main()