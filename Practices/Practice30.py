# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同

def f():
    a=input('输入一串数字:')
    b=a[ : :-1]

    if a==b:
        print('是回文')
    else:
        print('不是回文')

def f2():
    a=input('输入一串数字:')
    b=''.join(list(a))
    
    if a==b:
        print('是回文')
    else:
        print('不是回文')


def run():
    f2()


run()
