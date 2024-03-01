import turtle

turtle = turtle.Turtle()
turtle.speed(0)

def create_house():
    draw_rectangle(100, 100)
    reposition_turtle(100, 100)
    draw_triangle(100, 120)
    reposition_turtle(40, 0)
    draw_rectangle(40, 20)
    reposition_turtle(10, 50)
    draw_rectangle(20, 20)
    reposition_turtle(70, 50)
    draw_rectangle(20, 20)

def draw_rectangle(height, width):
    for i in range(2):
        turtle.forward(width)
        turtle.lt(90)
        turtle.forward(height)
        turtle.lt(90)

def draw_triangle(length, angle):
    for i in range(3):
        turtle.lt(angle)
        turtle.forward(length)

def reposition_turtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()

create_house()
turtle.mainloop()