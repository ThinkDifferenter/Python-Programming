# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵

import numpy as np

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]


def f():
    Z=np.zeros(shape=(len(X),len(X[0])))
    
    for i in range(len(X)):
        for j in range(len(X[0])):
            Z[i][j]=X[i][j]+Y[i][j]
    print(Z)



def f2():
        
    Z=[[],[],[]]
    
    for i in range(len(X)):
        for j in range(len(X[0])):
            Z[i].append(X[i][j]+Y[i][j])
    print(Z)


def f3():
    x=np.array(X)
    y=np.array(Y)
    z=x+y
    print(z)
    
def run():
    f3()

run()
