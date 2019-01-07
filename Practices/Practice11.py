# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
import time

def f(n):
    a=1
    b=1
    if n<=2:
        print('input error')
        return
        
    for i in range(1,n):
        a,b=b,a+b
    print(a)


def f2(n):
    a=1
    b=1
    if n<=2:
        print('input error')
        return
    
    for i in range(1,n):
        t=b
        b=a+b
        a=t
    print(a)

def f3(n):
    
    if n==1 or n==2:
        return 1
    else:
        return f3(n-1)+f3(n-2)

def run():
    s=time.clock()
    print(f3(20))
    e=time.clock()
    print(e-s)
    
    s=time.time()
    f2(20)
    e=time.time()
    print(e-s)
    
run()
    
