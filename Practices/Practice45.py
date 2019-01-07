# 统计 1 到 100 之和。

def f(low,up):
    s=0
    for i in range(low,up+1):
       s+=i
    print('%d-%d summary is ',s)

def run():
    low = int(input('Please input low:'))
    up = int(input('Please input up:'))
    f(low,up)


run()
    
