# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

def f(n):
    # 分子
    a=2
    b=3
    # 分母
    x=1
    y=2
    
    t=0
    for i in range(n):
        t+=float(a/x)
        a,b=b,a+b
        x,y=y,x+y
    return t

def run():
    print(f(2))

run()
