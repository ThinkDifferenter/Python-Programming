# 求1+2!+3!+...+20!的和。

import math
import time
def f(n):
    s=0
    for i in range(1,n+1):
        s+=math.factorial(i)

    return s


def run():
    print(f(20))

s=time.time()
run()
e=time.time()
print('运行时间:',e-s)
