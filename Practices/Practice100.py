# 列表转换为字典。

def f1():
    # 列表内字典创建
    i = ['a', 'b']
    l = [1, 2]
    print (dict([i,l]))
    #{'a': 'b', 1: 2}

def f2():
    # zip 列表间字典创建
    i = ['a','b','c']
    l = [1,2,3]
    b=dict(zip(i,l))
    print(b)
    # {'a': 1, 'b': 2, 'c': 3}


if __name__=='__main__':
    f2()

