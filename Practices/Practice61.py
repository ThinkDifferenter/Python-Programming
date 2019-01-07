# 打印出杨辉三角形（要求打印出10行如下图）。

# n为打印出来的字符串行数

import numpy as np
from sys import stdout

def f(n):
    
    # 利用numpy 创建数组
    a=np.zeros((n,n))
    
    '''
    手动创建数组
    a=[]
    for i in tange(n):
        a.append([])
        for j in range(n):
            a[i].append(0)
    '''

    for i in range(n):
        a[i][0]=1
        a[i][i]=1
    for i in range(2,10):
        for j in range(1,i):
            a[i][j] = a[i-1][j]+a[i-1][j-1]

    for i in range(n):
        for j in range(i+1):
            stdout.write(str(a[i][j]))
            stdout.write(' ')
        print()

            


    

if __name__=='__main__':

    lst()
    
    
