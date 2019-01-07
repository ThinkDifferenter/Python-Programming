# 字符串排序。


def strSort():

    l=[]
    
    a=input('Please input string1:')
    b=input('Please input string2:')
    c=input('Please input string3:')

    # 一次追加多个元素
    l.extend([a,b,c])

    l.sort()

    print(l)


if __name__=='__main__':
    strSort()
    
    
