# 暂停一秒输出，并格式化当前时间。

import time
import calendar

def f():

    i=1
    while(i<5):
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        time.sleep(1)


def f2():
    cal=calendar.month(2018,9)
    print(cal)
    
def run():
    #f()
    f2()

run()
    

