# 读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。

def Print(l):
    for i in range(len(l)):
        print('*'*l[i])


if __name__=='__main__':
    l=[1,2,3,4,5,6,7]

    Print(l)
    
