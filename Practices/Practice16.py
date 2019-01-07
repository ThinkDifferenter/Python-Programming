# 输出指定格式的日期

import datetime
import time


def dateFormate():

    print(datetime.date.today().strftime('%d/%m/%Y'))

    dateObject=datetime.date(1996,3,27)
    
    print(dateObject.strftime('%Y-%m-%d'))

    print(time.localtime())

    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

    
def run():
    dateFormate()


run()
 
