# 输入3个数a,b,c，按大小顺序输出。　

def f():
    l=[]
    a=int(input('输入数字1:'))
    b=int(input('输入数字2:'))
    c=int(input('输入数字3:'))

    l.append(a)
    l.append(b)
    l.append(c)
    
    l.sort()

    print(l)

if __name__=='__main__':
    f()
    
