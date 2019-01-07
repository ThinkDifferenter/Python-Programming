# 有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），
# 凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

def f():
    
    n = int(input('请输入总人数:'))
    
    num=[]
    for i in range(n):
        num.append(i+1)

    sum=0
    
    while True:
        t=0 # 记录已经抛出的元素个数
        for i in range(1,len(num)+1):
            sum+=1
            if sum%3==0:
                num.pop(i-1-t)
                t+=1
                
        if len(num) == 1:
            print('最后留下的是第%d位'%num[0])
            break


def f2():
    data=[i+1 for i in range(6)]
    print(data)
    i=1

    while len(data)>1:
        if i%3==0:
            data.pop(0)
        else:
            data.insert(len(data),data.pop(0))
        i+=1

    print('最后留下的是第%d位'%data[0])

    



if __name__ == '__main__':
    f2()
