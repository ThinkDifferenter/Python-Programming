# 求0—7所能组成的奇数个数。

def f():
    n=int(input('请输入组成的位数:'))
    s=1
    
    if n==1:
        print('0-7能够组成4个1位奇数')
    elif n==2:
        print('0-7能够组成28个2位奇数')
    else:
        l=[8]*n
        l[0]=7
        l[n-1]=4

        for i in range(len(l)):
            s*=l[i]
            
        print('0-7能够组成%d个%d位奇数'%(s,n))

if __name__=='__main__':
    f()
