# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

def f():
    l=[1,2,3,4,5,6]
    n=int(input('请输入一个数字:'))
    for i in range(len(l)):
        if l[i-1]<n<l[i]:
            l.insert(i,n)
        if n>l[len(l)-1]:
            l.append(n)
            
    print(l)
    

def run():
    f()

run()
