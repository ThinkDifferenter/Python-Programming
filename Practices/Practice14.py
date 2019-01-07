# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

import time

def f(n):
    l=[]
    while n>1:
        for i in range(2,n+1):
            if  n%i == 0:
                n=int(n/i)
                l.append(i)
                break
    return l

print(sum(f(6)))

def run():
    s = input("输入一个正整数:")
    # a='12.3' isdigit(a)-> false
    if s.isdigit() and int(s) > 0:
        print(s, "=", " * ".join([str(x) for x in f(int(s))]))
    else:
        print("请输入正确的正整数")


s=time.time()
run()
e=time.time()
print('the running time is ',e-s)


