# 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

from collections import deque

def Deque():
    m = 3
    a = [1,2,3,4,5,6,7]   # 7 个数
    print(a)
    f = deque(a)
    f.rotate(m)
    print (list(f))

def f():
    m=3
    a = [1,2,3,4,5,6,7]   # 7 个数
    print(a)
    l=len(a)
    m=l-m
    
    arr=[]
    arr=a[m:l]+a[0:m]
    print(arr)


if __name__=='__main__':
    f()
