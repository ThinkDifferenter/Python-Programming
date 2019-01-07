# 求一个3*3矩阵主对角线元素之和。

# 利用下标索引的方式
def f(l):
    sum=0
    for i in range(len(l)):
            sum += l[i][i]
    print(sum)

# 利用句柄（Python 支持二维list不同行的元素个数不同
def f2(l):
    sum=0
    for i in l:
        for j in i:
            if l.index(i) == i.index(j):
                sum += j
    print(sum)

def run():
    l=[[1,2,3],[4,5,6],[7,8,9]]
    f2(l)

run()
