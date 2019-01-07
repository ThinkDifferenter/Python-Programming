# 模仿静态变量的用法。

def varfunc():
    var = 0
    print ('var = %d' % var)
    var += 1

# 类的属性
class Static:
    StaticVar = 5

    def varfunc(self):
        self.StaticVar += 1
        print (self.StaticVar)

# 输出类的变量
print (Static.StaticVar)

# 创建类的对象
a = Static()

# 调用类的成员函数
for i in range(3):
    a.varfunc()
