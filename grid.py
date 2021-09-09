import turtle

count = 6
count2 = 6
i=1
j=1

turtle.penup()
turtle.goto(-300,-300)
turtle.pendown()

while(count>0):
    turtle.forward(500)
    turtle.penup()
    turtle.goto(-300,-300+i*100)
    turtle.pendown()
    i+=1
    count -= 1

turtle.penup()
turtle.goto(-300,-300)
turtle.pendown()

turtle.left(90)
while(count2>0):
    turtle.forward(500)
    turtle.penup()
    turtle.goto(-300+j*100,-300)
    turtle.pendown()
    j+=1
    count2 -= 1

turtle.exitonclick()
