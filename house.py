import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor ("sky blue")
#Function to Draw a Square 
def square (size,color):
  t.fillcolor (color)
  t. begin_fill()
  for i in range (4):
    t. forward (size)
    t.left (90)
  t. end_fill()  
#Function to Draw a Triangle
def triangle (size,color):
  t.fillcolor(color)
  t.begin_fill()
  for i in range (3):
   t.forward(size)
   t.left(120)
  t.end_fill()   

#Function to Draw a Rectangle

def rectangle (size2,size,color):
  t.fillcolor(color)
  t.begin_fill()
  for i in range (2):
    t.forward (size) 
    t.right (90)
    t.forward (size2) 
    t.right (90)
  t.end_fill()  

#function to move:
def move (number1,number2):
  t. penup()
  t.goto(number1,number2)
  t.pendown()
#House1
move(-200,-200)
square(150,"white")
move(-200,-50)
triangle(150 ,"brown")
move(-130,-100)
rectangle(100,70,"red")
move(-190,-150)
square(50,"blue")

move(200,-200)
square(150,"white")
move(200,-50)
triangle(150,"green")
move(220,-90)
square(40,"pink")
move(290,-90)
square(40,"pink")
move(290,-100)
rectangle(100,50,"green")

move(-200,-200)
for i in range (20):
  triangle (30,"green")
  t.forward(30)

