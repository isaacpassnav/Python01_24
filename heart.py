from turtle import *

bgcolor("blackgit ")
color("red")
title("MyDearly")
begin_fill()
pensize(3)
left(50)    
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()

penup()
goto(0, -50)
pendown()
color("red")
write(" I love you ;) ", align="center",
    font=("Brush Scrip TM", 45, "normal"))
hideturtle()
done()

