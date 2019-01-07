# 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

def f(l):
    print('交换前的数组:',l)

    min=l[0]
    max=l[0]
    
    for i in range(len(l)):
        if l[i]>max:
            max=l[i]
            l[0],l[i]=l[i],l[0]
            
        if l[i]<min:
            min=l[i]
            l[len(l)-1],l[i]=l[i],l[len(l)-1]        

    print('交换后的数组:',l)


def f():
    a=[1,4,52,6,72,9,32] # 注意同一个位置上的数据移动两次
    print (a)
    # 最小的放到最后
    Min = min(a)
    a.remove(Min)
    a.append(Min)
    # 最大的放到最前面
    Max = max(a)
    a.remove(Max)
    a.insert(0,Max)
    print (a)

if __name__=='__main__':
    l=[1,4,52,6,72,9,32]
    #f(l)
    f()

    

    
    
