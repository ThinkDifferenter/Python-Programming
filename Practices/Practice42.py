# 学习使用auto定义变量的用法。

# 全局变量
num = 2

def autofunc():
    # 局部变量-就近原则，使用距离操作最近的变量
    num = 1
    print ('internal block num = %d' % num)
    num += 1

for i in range(3):
    # 没有相应的局部变量，使用全局变量
    print ('The num = %d' % num)
    num += 1
    autofunc()
