import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
t.pensize(3)
n = 36
h = 0

for i in range(250):
    color = colorsys.hsv_to_rgb(h,1,0.8)
    t.pencolor(color)
    h+= 1/n
    t.right(i)
    t.circle(55,i)
    t.forward(i)
    t.left(91)

turtle.done()       
    