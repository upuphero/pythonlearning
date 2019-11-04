def foo():
  global a
  a = 200
 

if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 100