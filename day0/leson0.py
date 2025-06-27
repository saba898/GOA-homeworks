from turtle import *

#we want to print a house

#step 1:  draw a quare
speed(30)
width(7)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of squer

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)  
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing window
penup()
goto(40, 140)  #corner of the left window
setheading(0)
pendown()
color("blue")
begin_fill()
for _ in range(4):
    forward(30)
    left(90)
end_fill()   

#right window
penup()
goto(130, 140) #corner of the right window
setheading(0)
pendown()
color("blue")
begin_fill()
for _ in range(4):
    forward(30)
    left(90)
end_fill()







exitonclick()