# 请输入星期几的第一个字母来判断一下是星期几，
# 如果第一个字母一样，则继续判断第二个字母。


def f():
    s=input('输入星期英文的头字母(大写):')
    if s == 'M':
        print('星期一')
    elif s == 'W':
        print('星期三')
    elif s == 'F':
        print('星期五')
    elif s == 'T':
        y=input('请输入第二个字母（大写）')
        if y == 'U':
            print('星期二')
        else :
            print('星期四')
    elif s == 'S':
        y=input('请输入第二个字母（大写）')
        if s == 'U':
            print('星期天')
        else :
            print('星期六')


def run():
    f()

    
run()
    
