
#Creates screen and player 
import turtle 

p1 = turtle.Turtle() 

s = turtle.Screen()
s.setup(width=750,height=750) 

#user movement functions 

def go_up():
    p1.forward(50)

def go_down():
    p1.left(180)

def go_left():
    p1.left(90)  

def go_right():
    p1.right(90)

def stopmove():
    p1.penup() 

def gomove(): 
    p1.pendown()

#Imports user movement on screen 

s.onkeypress(go_up,"Up")
s.onkeypress(go_down,"Down")
s.onkeypress(go_left,"Left")
s.onkeypress(go_right,"Right")
s.onkeypress(stopmove,"space")
s.onkeypress(gomove,"v")

#Ends Function 
s.listen()
turtle.done()