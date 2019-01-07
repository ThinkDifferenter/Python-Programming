# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,
# 当输入n为奇数时，调用函数1/1+1/3+...+1/n

def Ou(n):
    r=0
    for i in range(2,n+1,2):
       r+=1/i
    return r


def Ji(n):
    r=0
    for i in range(1,n+1,2):
       r+=1/i
    return r

def select():
    
    n=int(input('Please input a number:'))
    r=0
    if n%2==0:
        print('The result is ',Ou(n))
    else:
        print('The result is ',Ji(n))




if __name__ == '__main__':
    select()



    
        
    
