import turtle
from turtle import *

turtle.title("3D designs in python")
turtle.speed(40)
turtle.bgcolor("white")


r,g,b=255,0,0

for i in range(255*2):
    colormode(255)
    if i<255//3:
        g+=3
    elif i<255*2//3:
        r-=3
    elif i<255:
        b+=3
    elif i<255*4//3:
        g-=3
    elif i<255*5//3:
        r+=3
    else:
        b-=3
    fd(70+i)
    rt(100)
    pencolor(r,g,b)

turtle.textinput("COPY CAT","Are u Subscriber of COPY CAT ©")
