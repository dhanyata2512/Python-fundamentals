import turtle
player = turtle.Turtle()
player.shape("turtle")
player.penup()
player.goto(-200,200)

end = turtle.Turtle()
end.shape("circle")
end.penup()
end.goto(180,-180)


t = turtle.Turtle()
t.speed(0)
# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

screen.bgcolor("violet")

def rectangle (x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()
  for i in range(2):
    t.forward(50)
    t.left(90)
    t.forward(200)
    t.left(90)

def up ():
  player.setheading(90)

def down ():
  player.setheading(-90)
  
def right ():
  player.setheading(0)

def left ():
  player.setheading(180)

def move ():
  player.forward(10)
  
   
rectangle(-150,0)
rectangle(0,-150)
rectangle(150,0)
t.hideturtle()
screen.listen()
screen.onkey (up,"Up")
screen.onkey(down,"Down")
screen.onkey(left,"Left")
screen.onkey(right,"Right")
screen.onkey(move,"space")


while True:
  if player.distance(end) < 5:
    print("You win")
    break

screen.mainloop()
