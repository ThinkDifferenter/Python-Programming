# 按相反的顺序输出列表的值。

def f():
    a=['one','two','three']
    print(' '.join(reversed(a)))

def f2():
    a=['one','two','three']
    print(a[: : -1])

def f3():
    a=['one','two','three']
    b=[]
    for i in range(0,len(a)):
        b.append(a[-(i+1)])
    print(b)
    
def run():
    f3()


run()
