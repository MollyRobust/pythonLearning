from turtle import *

def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        # 设置笔刷宽度:
        width(4)
        pencolor('red')
        fd(40)
        rt(144)

for x in range(0, 250, 50):
    drawStar(x, 0)

done()