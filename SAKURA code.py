import turtle as F
from random import *
from math import *
import time

def tree(n,l,f):
    f.pd()# draw tree branches
    # shadow effect
    t = cos(radians(f.heading()+45))/8+0.25
    f.pencolor(t,t,t)
    f.pensize(n/3)
    f.forward(l)# draw tree branches

    if n > 0:
        b = random() * 15 + 10  # right branch angle deviation
        c = random() * 15 + 10  # left branch angle deviation
        d = l * (random() * 0.25 + 0.7)  # length of next branch
        # right turn a certain angle and draw right branch
        f.right(b)
        tree(n - 1, d, f)
        # left turn a certain angle and draw left branch
        f.left(b + c)
        tree(n - 1, d, f)
        # turn back
        f.right(c)
    else:
        # draw leaf
        f.right(90)
        n=cos(radians(f.heading()-45))/4+0.5
        f.pencolor(n,n*0.8,n*0.8)
        f.circle(3)
        f.left(90)
    f.pu()
    f.backward(l)#move back
    w.update() #show the whole process
    #time.sleep(0.001) #speed

# drawing area
f = F.Turtle()
# screen size
w = F.Screen()

w.bgcolor(0.5, 0.5, 0.5) # background color
f.ht() # hide turtle
f.speed(0) # speed: 1-10 gradually, 0 is the fastest
w.tracer(0, 0) # stop auto-update

def start_drawing(x, y):
    w.onscreenclick(None)  # remove click event binding
    f.pu()#pen start
    f.backward(100)
    f.left(90)  # left turn 90 degrees
    f.pu()  # pen up
    f.backward(300)  # move back 300
    tree(12, 100, f)  # recursive 7 layers


def falling_petal(f):
    f.pu()
    f.goto(0, 100)
    for i in range(1000):
        if random() > 0.1:
            f.pu()
            # petal fall
            t = f.heading()
            an = -40 + random() * 40
            f.setheading(an)
            dis = int(1000 * random() * 0.5 + 400 * random() * 0.3 + 200 * random() * 0.2)
            f.forward(dis)
            f.setheading(t)
            # leaf
            f.pd()
            f.right(90)
            n = cos(radians(f.heading() - 45)) / 4 + 0.5
            f.pencolor(n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 + n * 0.4)
            f.circle(4, 36)
            w.update()
            time.sleep(0.01)  # Add
            f.left(90)
            f.pu()

            t = f.heading()
            f.setheading(an)
            f.backward(dis)
            f.setheading(t)
    f.pencolor("black")
    f.goto(50, -300)
    f.write("Tree drawing completed!", align="center", font=("Times New Roman", 16, "normal"))



f.pu()
f.backward(100)
f.left(90)#left rotate 90degree
f.pu()
f.backward(300)#back 300
tree(12,100,f)#递归7层
falling_petal(f)
F.done()
