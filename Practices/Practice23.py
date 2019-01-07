# 打印出如下图案（菱形）:

from sys import stdout
def f():
    # 绘制菱形上部分
    for i in range(0,4):
        for j in range(2-i+1):
            stdout.write(' ')
        for k in range(2*i+1):
            stdout.write('*')
        print()
    #绘制菱形下部分
    for i in range(0,3):
        for j in range(i+1):
            stdout.write(' ')
        for k in range(4-2*i+1):
            stdout.write('*')
        print()


def f2():
    for i in range(4):
        print((3-i)*' '+(2*i+1)*'*')
    for i in range(3):
        print((i+1)*' '+(5-2*i)*'*')

def run():
    f2()

run()
    
