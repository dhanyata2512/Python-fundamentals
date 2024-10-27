
import turtle

t = turtle.Turtle()

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

screen.bgcolor("light blue")
t.shape("turtle")

def up ():
  t.setheading(90)

def down ():
  t.setheading(-90)

def right ():
  t.setheading(0)

def left ():
  t.setheading(180)

steps= int(input("How many steps do you want to move?\n"))

def move ():
  t.forward(steps)

def click (x,y):
  t. goto (x,y)

def drag (x,y):
  screen.tracer(0)
  t.goto (x,y)
  screen.tracer(1)
  
screen.listen()
screen.onkey(up,"Up")
screen.onkey (down,"Down")
screen.onkey (right,"Right")
screen.onkey(left,"Left")
screen.onkey(move,"space")
screen.onclick(click)
t.ondrag(drag)

screen.mainloop()
