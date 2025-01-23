from turtle import * # type: ignore

pencolor("yellow")
pensize(10)
shape("turtle")#triangle square turtle arrow

fillcolor("yellow")
begin_fill()
circle(50)
end_fill()

penup()
forward(200)
pendown()

fillcolor("blue")
pencolor("red")
begin_fill()
circle(30)
end_fill()

done()