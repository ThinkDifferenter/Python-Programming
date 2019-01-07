# 斐波那契数列

def fib(n):

    i=1
    j=1
    if n<=1:
        print(1)
    if n>=2:
        print(1)
        print(1)
        
    for index in range(1,n-1):
        i,j=j,i+j
        print(j)

def fib2(n):

    i=1
    j=1
    if n<=1:
        print(1)
    if n>=2:
        print(1)
        print(1)
        
    for index in range(1,n-1):
        t=j
        j=i+j;
        i=t
        print(j)


def run():
    n = int(input('输入斐波那契数列的位数:'));
    fib2(n)


run()
    
