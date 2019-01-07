# 画图，学用rectangle画方形。　　

import turtle as tt

# 参数n多边形边数
def drawLine(n):
    t=tt.Pen()
    t.color('yellow')
    t.width(3)
    t.begin_fill()
    t.shape('turtle')

    for i in range(n):
        t.forward(100)
        t.left(360/n)
    t.end_fill()    

def drawRactangle():
    t=tt.Pen()
    t.color('blue')
    t.width(3)
    t.shape('turtle')

    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()


    
def run():
    #drawLine(8)
    drawRactangle()
    
run()
