# 输入三个整数x,y,z，请把这三个数由小到大输出。

def f(i,j,k):
    if i>j and i>k:
        return i
    
    if j>i and j>k:
        return j

    if k>i and k>j:
        return k

def f2(i,j,k):
    if i>j:
        if i>k:
            return i
        else :
            return k
    else:
        if j>k:
            return j
        else:
            return k


def f3(i,j,k):
    a=i if i>j else j
    return a if a>k else k

    

def run():
    i=input('input i:')
    j=input('input j:')
    k=input('input k:')
    print('最大值为：%d\n' % int(f3(i,j,k)))


run()
    
