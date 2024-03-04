import turtle


def main():
    global t
    t = turtle.Turtle()
    t.speed(5)

    create_house()
    create_tractor()


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


def create_tractor():
    # Main box
    reposition_turtle(-200, 0)
    draw_rectangle(50, 100)
    # Cabin
    reposition_turtle(-140, 50)
    draw_rectangle(40, 40)
    reposition_turtle(-135, 55)
    draw_rectangle(30, 15)
    reposition_turtle(-145, 90)
    draw_rectangle(5, 50)
    # Spout
    reposition_turtle(-190, 50)
    draw_rectangle(30, 10)
    # Wheels
    reposition_turtle(-190, -15)
    draw_circle(25)
    reposition_turtle(-120, -15)
    draw_circle(30)
    reposition_turtle(-190, -3)
    draw_circle(12.5)
    reposition_turtle(-120, -3)
    draw_circle(17)


def draw_rectangle(height, width):
    for i in range(2):
        t.forward(width)
        t.lt(90)
        t.forward(height)
        t.lt(90)


def draw_triangle(length, angle):
    for i in range(3):
        t.lt(angle)
        t.forward(length)


def draw_circle(radius):
    t.circle(radius)


def reposition_turtle(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()


if __name__ == "__main__":
    main()
    turtle.done()