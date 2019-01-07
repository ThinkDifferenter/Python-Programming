# 编写input()和output()函数输入，输出5个学生的数据记录。

class Student:
    name=''
    age=0
    score=[None]*4

    def input(self):
        self.name=input('请输入姓名:')
        self.age=input('请输入年龄:')

        for i in range(len(self.score)):
            self.score[i]=int(input('请输入第%d门成绩'%(i+1)))

    def output(self):
        print('姓名:',self.name)
        print('年龄:',self.age)

        for i in range(len(self.score)):
            print('请输入第%d门成绩:%s'%((i+1),self.score[i]))

if __name__=='__main__':
    N = 1
    studentArray = [Student()] * N
    for i in range(len(studentArray)):
        studentArray[i].input()

    for i in range(len(studentArray)):
        studentArray[i].output()
