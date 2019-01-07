# 输入某年某月某日，判断这一天是这一年的第几天？
import time

def f():
    
    year=int(input("年：\n"))
    month=int(input("月：\n"))
    day=int(input("日：\n"))
    months1=[0,31,60,91,121,152,182,213,244,274,305,335,366] #闰年
    months2=[0,31,59,90,120,151,181,212,243,273,304,334,365] #平年

    if ((year%4==0)and(year%100!=0)) or((year%100==0)and(year%400==0)):
        Dth=months1[month-1]+day
    else:
        Dth=months2[month-1]+day
    print ("是该年的第%d天"%Dth)


def f2():
    
    D=input("请输入年份，格式如XXXX-XX-XX：")
    d=time.strptime( D,'%Y-%m-%d').tm_yday
    print ("the {} day of this year!".format(d))


f2()


