# 判断101-200之间有多少个素数，并输出所有素数。

import math

def f():
    flag=1    
    for i in range(101,201):
        for j in range(2,int(math.sqrt(i)+1)):
            if i%j == 0:
                flag=0
                break
        if flag==1:
            print(i)
            
def f2():
    l = []
    for i in range(101,200):
        for j in range(2,int(math.sqrt(i)+1)):
            if i%j ==0:
                break
        else:
            l.append(i)

    print(l)
    print("总数为：%d" % len(l))

def run():
    f()


run()
            
        
