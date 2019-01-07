# 输出 9*9 乘法口诀表

def f():
    for i in range(1,10):
        for j in range(1,10):
            #print('%d*%d=%d\t'%(i,j,i*j))
            #print(i,'*',j,'=',i*j)
            print('{}*{}={}'.format(i,j,i*j))
        print()

def run():
    f()
    print('asd',end=' ')
    print('asd')
    
    


run()
