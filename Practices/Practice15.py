# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

def f(n):
    
    if n<60:
        return 'C'
    elif n>=90:
        return 'A'
    else:
        return 'B'

def run():
    a=int(input('please input score:'))
    b='you get level '+ f(a)
    print(b)
    
run()
