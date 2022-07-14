from turtle import*
import colorsys

speed(0)
bgcolor('black')
h = 0.0
pensize(2)

for i in range(300):
   col = colorsys.hsv_to_rgb(h,1,0.8)
   pencolor(col)
   h+=0.005
   circle(190-i, 30)
   rt(20)
   rt(120)
   circle(190-i,30)