# 输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

def f():
    a=int(input('输入一个奇数:'))
    cnt=1
    n=9
    
    while True:
        if n%a==0:
            print('%d 个 9 可以被 %d 整除 : %d'%(cnt,a,n))
            break
        else:
            n=n*10+9
            cnt+=1



if __name__=='__main__':
    f()

    
    

    
