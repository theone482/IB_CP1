#Iv 2nd race turtle
import turtle
import random
# make the finish line
turtle.color("white")
turtle.forward(300)
turtle.color("black")
turtle.left(90)
turtle.forward(450)
turtle.right(180)
turtle.forward(800)
turtle.penup()
turtle.goto(-450,0)
turtle.color("white")
turtle.pendown

screen = turtle.Screen()
screen.setup()
screen.title("turtle race")
# make five turtle
t1 = turtle.Turtle()
t1.shape("turtle")
t1.teleport(-450,0)
t1.color("green")

t3 = turtle.Turtle()
t3.shape("turtle")
t3.teleport(-450,200)
t3.color("blue")

t2 = turtle.Turtle()
t2.shape("turtle")
t2.teleport(-450,100)
t2.color("pink")

t4 = turtle.Turtle()
t4.shape("turtle")
t4.teleport(-450,-100)
t4.color("red")

t5 = turtle.Turtle()
t5.shape("turtle")
t5.teleport(-450,-200)
t5.color("purple")
while True:
    t5.forward(random.randint(1,10))
    
# make thgeme different colors
turtle.done()