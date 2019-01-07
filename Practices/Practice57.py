# 画图，学用line画直线。

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

def run():
    drawLine(8)

run()
