
import turtle
import random
# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

t = turtle.Turtle()
t.speed(0)
screen.bgcolor("black")
screen.colormode(255)

for i in range(15):
  x=random.randint (-200,200)
  y=random.randint (-200,200)
  t.penup()
  t.goto(x,y)
  t.pendown()
  r=random.randint (0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  t.pencolor(r,g,b)
  for i in range(36):
    a=random.randint(30,50)
    t.forward(a)
    t.backward(a)
    t.right(10)
    
