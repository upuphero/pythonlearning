def fac(num):
    if num == 0:
        return 1
    return num * fac(num - 1)

def main():
    n=int(fac(5))
    print(n)
    
if __name__ == "__main__":
    main()