# 暂停一秒输出。
import time

def f():
    a=[1,2,3,4,5]

    for i in range(0,len(a)):
        print(a[i])
        time.sleep(1)
    print('view over')
    
def run():
    f()

run()
