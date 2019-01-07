# 求输入数字的平方，如果平方运算后小于 50 则退出

def f(n):
    return n**2


def run():
    while True:
        n=int(input('Please input a number :'))
        if f(n)<50:
            print('The square of n is :',f(n))
            break
        else :
            print('The square of n is :',f(n))


run()
