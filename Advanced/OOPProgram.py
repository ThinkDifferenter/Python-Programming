def f1():
    # 实例方法：只能通过实例对象调用
    # 因为实例方法第一个定义的参数必须是实例对象本身。
    class Myclass:
      def foo(self):
        print(id(self),'foo')   #id()是获取对象的空间地址

    a=Myclass()#既然是实例对象，那就要创建实例
    a.foo()#输出类里的函数地址
    print(id(a))#输出类对象的地址

def f2():
    # 类方法：定义类方法，要使用装饰器@classmethod，
    # 定义的第一个参数一定是类的引用，不过可以通过类或者实例的引用。
    class Myclass:
        @classmethod#类方法装饰器
        def foo2(self):
            print(id(self),'foo2')  

    print(id(Myclass))  #类对象，直接可以调用，不需要实例化。这句说明了类也是有存储空间的
    Myclass.foo2()      #类方法，直接可以调用，不需要实例化对象


def f3():
    # 定义静态方法使用装饰器@staticmethod，没有默认的必须参数，
    # 可以通过类和实例直接调用。静态方法就如同类外函数一样。
    # 若在静态函数内访问类变量也是需要 类名.变量名 的方式访问。
    class Myclass:
      @staticmethod#静态方法
      def foo3():   #没有self参数
        print('foo3')

    Myclass.foo3()   #通过类调用
    a=Myclass()
    a.foo3()       #通过实例调用
    #结果foo3

def f4():
    #'所有员工的基类'
    class Employee:  
        empCount = 0
        # 第一种方法__init__()方法是一种特殊的方法，
        # 被称为类的构造函数或初始化方法，当创建了这个类的实例时
        # 就会先为实例对象开辟空间，添加到类对象的引用，然后就会调用该方法。
        #（其实是先调用的__new__方法，再调用的__init__方法）
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary
            Employee.empCount += 1

        def displayCount(self):
            print("TotalEmployee %d" % Employee.empCount)

        def displayEmployee(self):
            print("Name: ", self.name, ", Salary: ", self.salary)

    #"创建 Employee 类的第一个对象"
    emp1 = Employee("Zara", 2000)
    #"创建 Employee 类的第二个对象"
    emp2 = Employee("Manni", 5000)
    emp1.displayEmployee()
    emp2.displayEmployee()
    print ("TotalEmployee %d" % Employee.empCount)


def f5():
    class Parent:       # 定义父类
        parentAttr = 100
        def __init__(self):
            print("调用父类构造函数")
        def parentMethod(self):
            print('调用父类方法')
        def setAttr(self, attr):
            Parent.parentAttr = attr
        def getAttr(self):
            print("父类属性 :", Parent.parentAttr)
    # 如果在继承元组中列了一个以上的类，那么它就被称作”多重继承” 
    class Child(Parent):
        # 定义子类
        def __init__(self):
            print("调用子类构造方法")  # 无论子类还是父类，都要单独写一次_init_
        def childMethod(self):
            print('调用子类方法')
        def getAttr(self):
            print('重写父类方法，因为父类方法不能满足需求')


    c = Child()  # 实例化子类
    c.childMethod()  # 调用子类的方法
    c.parentMethod()  # 调用父类方法
    c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
    # 如果父类方法的功能不能满足需求，可以在子类重写父类的方法。
    # 实例对象调用方法时会调用其对应子类的重写后的方法
    c.getAttr()  # 再次调用父类的方法 - 获取属性值

def f6():
    '''__foo__: 定义的是特列方法，类似 __init__() 之类的。
    _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
    __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。'''
    
    class JustCounter:
        __secretCount = 0    # 私有变量
        publicCount = 0      # 公开变量
        def count(self):
            self.__secretCount += 1
            self.publicCount += 1
            print(self.__secretCount)  # 在内部使用私有化属性，不会产生错误

    counter = JustCounter()
    counter.count()
    counter.count()
    print(counter.publicCount)
    # print(counter.__secretCount) # 报错，实例不能访问私有变量


if __name__=='__main__':
    f6()
