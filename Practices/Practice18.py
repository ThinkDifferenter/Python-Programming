# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222
# (此时共有5个数相加)，几个数相加由键盘控制。

from functools  import reduce

def f():
    #输入
    a=int(input('Please input a:'))
    n=int(input('Please input n:'))

    # 获得n个数值
    sn=[]
    tn=0
    for i in range (1,n+1):
        tn=tn+a
        a=a*10
        sn.append(tn)
        print(tn)

    # 对n个数值进行求和
    '''
    S=0
    for j in range(0,len(sn)):
        S+=sn[j]

    print('The sum is',S)
    '''
    
    print(type(sn))
    sn = reduce(lambda x,y : x + y,sn)
    print(type(sn))
    print('The sum is',sn)

def run():
    f()



run()

        
