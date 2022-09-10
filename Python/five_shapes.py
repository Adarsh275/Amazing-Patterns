# Five different shapes in one code

import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")

astroid = turtle.Turtle()
astroid.speed(0)
traid = turtle.Turtle()
traid.speed(0)
traid.up
traid.goto(-120,120)
traid.down()
squad = turtle.Turtle()
squad.speed(0)
squad.up()
squad.goto(120,120)
squad.down()
pentagon = turtle.Turtle()
pentagon.speed(0)
pentagon.up()
pentagon.goto(-120,-120)
pentagon.down()
octagon = turtle.Turtle()
octagon.speed(0)
octagon.up()
octagon.goto(120,-120)
octagon.down()
colors = ["red","green","yellow","blue","cyan","pink","Orange","white","lightgreen"]

for i in range(50):
   astroid.color(random.choice(colors))
   astroid.forward(i*3)
   astroid.left(144)

for i in range(50):
   traid.color(random.choice(colors))
   traid.forward(i*3)
   traid.left(120)

for i in range(50):
   squad.color(random.choice(colors))
   squad.forward(i*2)
   squad.left(98)

for i in range(50):
   pentagon.color(random.choice(colors))
   pentagon.forward(i*2)
   pentagon.left(72)

for i in range(75):
   octagon.color(random.choice(colors))
   octagon.forward(i)
   octagon.left(68)

traid.up()
traid.goto(-110,200)
traid.down()
traid.write("Triad")
traid.hideturtle()   

squad.up()
squad.goto(120,180)
squad.down()
squad.write("Squad")
squad.hideturtle()   

pentagon.up()
pentagon.goto(-140,-20)
pentagon.write("Pentagon")
pentagon.hideturtle()   

octagon.up()
octagon.goto(120,-40)
octagon.down()
octagon.write("Hexagon")
octagon.hideturtle()   

astroid.up()
astroid.goto(0,60)
astroid.down()
astroid.write("Astroid")
astroid.hideturtle()   

turtle.done()  