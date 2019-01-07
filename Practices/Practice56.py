# 画图，学用circle画圆形。　　

import turtle as tt
import math as mt
import matplotlib.pyplot as plt

def f():
    tt.title('画圆')          #画布标题
    tt.setup(1000,800,0,0)    #画布大小及初始位置
    pen=tt.Turtle()           #创建画笔
    pen.color('red')          #画笔颜色
    pen.width(2)              #画笔宽度
    pen.shape('turtle')       #画笔形状
    pen.speed(1)              #画笔速度
    pen.circle(100)           #画圆大小


def f2():
    x=[]
    y=[]

    for a in range(1,11):
        for b in range(0,360):
            x.append(a*(mt.cos(mt.pi*(b/180))))
            y.append(a*(mt.sin(mt.pi*(b/180))))

    plt.scatter(x,y,s=30)
    plt.axis([-11,11,-11,11])
    plt.axis('equal')
    plt.show()
            

def run():
    f2()


run()
    
