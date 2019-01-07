# 利用递归方法求5!。

import math
import time

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

def run():
    print(fac(30))

s=time.time()
run()
e=time.time()
print(e-s)

s=time.time()
print(math.factorial(30))
e=time.time()
print(e-s)

