# coding:utf-8
"""
这个文件用来学习turtle绘制图片的脚本，绘制小猪佩琪
Reference: https://docs.python.org/3/library/turtle.html

绘制一个小乌龟：
https://www.cnblogs.com/bravestarrhu/p/8287261.html
"""
import turtle as t


class PaggyPink():
    def __init__(self):
        self.ttl = t
        self.ttl.screensize(400, 300, "blue")
        self.ttl.pensize(4)  # 设置画笔的大小
        self.ttl.colormode(255)  # 设置GBK颜色范围为0-255
        self.ttl.color((255, 155, 192), "pink")  # 设置画笔颜色和填充颜色(pink)
        self.ttl.setup(840, 500)  # 设置主窗口的大小为840*500
        self.ttl.speed(10)  # 设置画笔速度为10

    def getPaggy(self):
        self.draw_paggynose()
        self.draw_paggyhead()
        self.draw_paggyear()
        self.draw_paggyeye()
        self.draw_paggycheek()
        self.draw_paggymouth()
        self.draw_paggybody()
        self.draw_paggyhand()
        self.draw_paggyfoot()
        self.draw_paggynil()
        self.ttl.done()

    def draw_paggynose(self):
        self.ttl.pu()  # 提笔
        self.ttl.goto(-100, 100)  # 画笔前往坐标(-100,100)
        self.ttl.pd()  # 下笔
        self.ttl.seth(-30)  # 笔的角度为-30°
        self.ttl.begin_fill()  # 外形填充的开始标志
        a = 0.4
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a = a + 0.08
                self.ttl.lt(3)  # 向左转3度
                self.ttl.fd(a)  # 向前走a的步长
            else:
                a = a - 0.08
                self.ttl.lt(3)
                self.ttl.fd(a)
        self.ttl.end_fill()  # 依据轮廓填充
        self.ttl.pu()  # 提笔
        self.ttl.seth(90)  # 笔的角度为90度
        self.ttl.fd(25)  # 向前移动25
        self.ttl.seth(0)  # 转换画笔的角度为0
        self.ttl.fd(10)
        self.ttl.pd()
        self.ttl.pencolor(255, 155, 192)  # 设置画笔颜色
        self.ttl.seth(10)
        self.ttl.begin_fill()
        self.ttl.circle(5)  # 画一个半径为5的圆
        self.ttl.color(160, 82, 45)  # 设置画笔和填充颜色
        self.ttl.end_fill()
        self.ttl.pu()
        self.ttl.seth(0)
        self.ttl.fd(20)
        self.ttl.pd()
        self.ttl.pencolor(255, 155, 192)
        self.ttl.seth(10)
        self.ttl.begin_fill()
        self.ttl.circle(5)
        self.ttl.color(160, 82, 45)
        self.ttl.end_fill()

    # 头
    def draw_paggyhead(self):
        self.ttl.color((255, 155, 192), "pink")
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(41)
        self.ttl.seth(0)
        self.ttl.fd(0)
        self.ttl.pd()
        self.ttl.begin_fill()
        self.ttl.seth(180)
        self.ttl.circle(300, -30)  # 顺时针画一个半径为300,圆心角为30°的园
        self.ttl.circle(100, -60)
        self.ttl.circle(80, -100)
        self.ttl.circle(150, -20)
        self.ttl.circle(60, -95)
        self.ttl.seth(161)
        self.ttl.circle(-300, 15)
        self.ttl.pu()
        self.ttl.goto(-100, 100)
        self.ttl.pd()
        self.ttl.seth(-30)
        a = 0.4
        for i in range(60):
            if 0 <= i < 30 or 60 <= i < 90:
                a = a + 0.08
                self.ttl.lt(3)  # 向左转3度
                self.ttl.fd(a)  # 向前走a的步长
            else:
                a = a - 0.08
                self.ttl.lt(3)
                self.ttl.fd(a)
        self.ttl.end_fill()

    # 耳朵
    def draw_paggyear(self):
        self.ttl.color((255, 155, 192), "pink")
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(-7)
        self.ttl.seth(0)
        self.ttl.fd(70)
        self.ttl.pd()
        self.ttl.begin_fill()
        self.ttl.seth(100)
        self.ttl.circle(-50, 50)
        self.ttl.circle(-10, 120)
        self.ttl.circle(-50, 54)
        self.ttl.end_fill()

        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(-12)
        self.ttl.seth(0)
        self.ttl.fd(30)
        self.ttl.pd()
        self.ttl.begin_fill()
        self.ttl.seth(100)
        self.ttl.circle(-50, 50)
        self.ttl.circle(-10, 120)
        self.ttl.circle(-50, 56)
        self.ttl.end_fill()

    # 眼睛
    def draw_paggyeye(self):
        self.ttl.color((255, 155, 192), "white")
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(-20)
        self.ttl.seth(0)
        self.ttl.fd(-95)
        self.ttl.pd()
        self.ttl.begin_fill()
        self.ttl.circle(15)
        self.ttl.end_fill()
        self.ttl.color("black")
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(12)
        self.ttl.seth(0)
        self.ttl.fd(-3)
        self.ttl.pd()
        self.ttl.begin_fill()
        self.ttl.circle(3)
        self.ttl.end_fill()

        self.ttl.color((255, 155, 192), "white")
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(-25)
        self.ttl.seth(0)
        self.ttl.fd(40)
        self.ttl.pd()
        self.ttl.begin_fill()
        self.ttl.circle(15)
        self.ttl.end_fill()
        self.ttl.color("black")
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(12)
        self.ttl.seth(0)
        self.ttl.fd(-3)
        self.ttl.pd()
        self.ttl.begin_fill()
        self.ttl.circle(3)
        self.ttl.end_fill()

    # 腮
    def draw_paggycheek(self):
        self.ttl.color((255, 155, 192))
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(-95)
        self.ttl.seth(0)
        self.ttl.fd(65)
        self.ttl.pd()
        self.ttl.begin_fill()
        self.ttl.circle(30)
        self.ttl.end_fill()

    # 嘴
    def draw_paggymouth(self):
        self.ttl.color(239, 69, 19)
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(15)
        self.ttl.seth(0)
        self.ttl.fd(-100)
        self.ttl.pd()
        self.ttl.seth(-80)
        self.ttl.circle(30, 40)
        self.ttl.circle(40, 80)

    # 身体
    def draw_paggybody(self):
        self.ttl.color("red", (255, 99, 71))
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(-20)
        self.ttl.seth(0)
        self.ttl.fd(-78)
        self.ttl.pd()
        self.ttl.begin_fill()
        self.ttl.seth(-130)
        self.ttl.circle(100, 10)
        self.ttl.circle(300, 30)
        self.ttl.seth(0)
        self.ttl.fd(230)
        self.ttl.seth(90)
        self.ttl.circle(300, 30)
        self.ttl.circle(100, 3)
        self.ttl.color((255, 155, 192), (255, 100, 100))
        self.ttl.seth(-135)
        self.ttl.circle(-80, 63)
        self.ttl.circle(-150, 24)
        self.ttl.end_fill()

    # 手
    def draw_paggyhand(self):
        self.ttl.color((255, 155, 192))
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(-40)
        self.ttl.seth(0)
        self.ttl.fd(-27)
        self.ttl.pd()
        self.ttl.seth(-160)
        self.ttl.circle(300, 15)
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(15)
        self.ttl.seth(0)
        self.ttl.fd(0)
        self.ttl.pd()
        self.ttl.seth(-10)
        self.ttl.circle(-20, 90)
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(30)
        self.ttl.seth(0)
        self.ttl.fd(237)
        self.ttl.pd()
        self.ttl.seth(-20)
        self.ttl.circle(-300, 15)
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(20)
        self.ttl.seth(0)
        self.ttl.fd(0)
        self.ttl.pd()
        self.ttl.seth(-170)
        self.ttl.circle(20, 90)

    def draw_paggyfoot(self):
        # 脚
        self.ttl.pensize(10)
        self.ttl.color((240, 128, 128))
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(-75)
        self.ttl.seth(0)
        self.ttl.fd(-180)
        self.ttl.pd()
        self.ttl.seth(-90)
        self.ttl.fd(40)
        self.ttl.seth(-180)
        self.ttl.color("black")
        self.ttl.pensize(15)
        self.ttl.fd(20)
        self.ttl.pensize(10)
        self.ttl.color((240, 128, 128))
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(40)
        self.ttl.seth(0)
        self.ttl.fd(90)
        self.ttl.pd()
        self.ttl.seth(-90)
        self.ttl.fd(40)
        self.ttl.seth(-180)
        self.ttl.color("black")
        self.ttl.pensize(15)
        self.ttl.fd(20)

    def draw_paggynil(self):
        # 尾巴
        self.ttl.pensize(4)
        self.ttl.color((255, 155, 192))
        self.ttl.pu()
        self.ttl.seth(90)
        self.ttl.fd(70)
        self.ttl.seth(0)
        self.ttl.fd(95)
        self.ttl.pd()
        self.ttl.seth(0)
        self.ttl.circle(70, 20)
        self.ttl.circle(10, 330)
        self.ttl.circle(70, 30)


if __name__ == '__main__':
    pp = PaggyPink()
    pp.getPaggy()
