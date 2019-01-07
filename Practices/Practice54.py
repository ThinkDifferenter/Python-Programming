# 取一个整数a从右端开始的4〜7位。

def f(n):
    t=0
    l=[]
    while n>=1:
        t=n%10
        n=int(n/10)
        l.append(t)
    print(l)
    for i in range(6,2,-1):
        print(i)


    
def run():
    f(123456789)



run()
        
