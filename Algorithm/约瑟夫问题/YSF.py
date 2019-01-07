# 约瑟夫问题

import time

# 模拟报数过程
def simulationWay():
        
    n=int(input("输入参与人数:"))
    m=int(input('输入出列位置:'))
    
    # 构造人员编号
    List=[]
    for i in range(1,n+1):
        List.append(i)

    # 报数指示变量
    sum=0

    while True: #多次报数
        
        # 记录本轮报数抛出的元素个数
        t=0;

        # 开始一轮报数（报数到3立马出队列，一轮报数中len(List)的动态改变）
        for i in range(1,len(List)+1):
            # 报数加一
            sum=sum+1
            
            if (sum)%m==0:
        #        print('i=',i,'sum=',sum,'\ti-1-t=',(i-1-t),\
        #              '\t抛出元素:',List[i-1-t],end=' ')
                List.pop(i-1-t)
        #        print('\t此时链表为:',List)
                t=t+1

        #print('这一轮报数结束啦!\t最后报数为:',sum,'\n')
        #time.sleep(3)

        if len(List)==1:
            print("最后留下的是原来第%d号的那位" % List[0])
            break


# 数学推导方式
def mathematicsWay():

    n=int(input("输入参与人数:"))
    m=int(input('输入出列位置:'))
    s=0
    
    for i in range(2,n+1):
        s=(s+m)%i

    print('最后出列的人初始位置为:',(s+1))





if __name__=='__main__':
    mathematicsWay()
    simulationWay()
