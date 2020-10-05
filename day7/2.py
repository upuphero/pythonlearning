import time


def main():
    # 一次性读取整个文件内容
    with open('2.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('2.txt', mode='r',encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print("\n2")
    print()

    # 读取文件按行读取到列表中
    with open('2.txt','r',encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)
    

if __name__ == '__main__':
    main()