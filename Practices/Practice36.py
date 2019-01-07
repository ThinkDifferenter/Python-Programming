# 求100之内的素数

import math

def f(low,up):
    
    for i in range(low,up+1):
        for j in range(2,int(math.sqrt(i)+1)):
            if(i%j==0):
                break
        else:
            print(i)


def f2(low,up):    
    for i in range(low,up+1):
        flag=True # 注意变量的作用域
        for j in range(2,int(math.sqrt(i)+1)):
            if(i%j==0):
                flag=False
                break
        if flag:
            print(i)

def run():
    f2(2,100)

run()
