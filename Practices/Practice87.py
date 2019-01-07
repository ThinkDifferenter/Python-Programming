# 回答结果（结构体变量传递）

class student:
    name=''
    age=0

    def Print(self):
        print('姓名:',self.name,'\t年龄:',self.age)

    


if __name__=='__main__':
    s=student()
    s.name='蒋军'
    s.age=22

    s.Print()


