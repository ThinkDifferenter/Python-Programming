# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

def f(n):
    l=[]
    t=0
    while n>=1:
        t=n%10
        n=int(n/10)
        l.append(t)
    print('位数:',len(l))
    print('逆序输出:',l)

def run():
    f(123)

run()
