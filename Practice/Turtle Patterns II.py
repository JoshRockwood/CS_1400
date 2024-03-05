import sys
import turtle


def main():
    t = turtle.Turtle()
    t.speed(5)

    command = int(sys.argv[1])

    if command == 1:
        create_house(t, scale_factor = 1.5, main_color = 'red')
        create_tractor(t, scale_factor = 0.8)
    elif command == 2:
        create_house(t, scale_factor = 1)
        create_tractor(t, scale_factor = 1)
    elif command == 3:
        create_house(t, scale_factor = 0.8)
        create_tractor(t, scale_factor = 1.5, main_color = 'orange')


def create_house(t, scale_factor = 1.0, main_color = 'burlywood'):
    # Main box
    t.fillcolor(main_color)
    t.begin_fill()
    draw_rectangle(t, 100 * scale_factor, 100 * scale_factor)
    t.end_fill()
    # Roof
    reposition_turtle(t, 100 * scale_factor, 100 * scale_factor)
    t.fillcolor('dark gray')
    t.begin_fill()
    draw_triangle(t, 100 * scale_factor, 120)
    t.end_fill()
    # Door
    reposition_turtle(t, 40 * scale_factor, 0 * scale_factor)
    t.fillcolor('cornflower blue')
    t.begin_fill()
    draw_rectangle(t, 40 * scale_factor, 20 * scale_factor)
    t.end_fill()
    # Windows
    reposition_turtle(t, 10 * scale_factor, 50 * scale_factor)
    t.fillcolor('alice blue')
    t.begin_fill()
    draw_rectangle(t, 20 * scale_factor, 20 * scale_factor)
    t.end_fill()
    reposition_turtle(t, 70 * scale_factor, 50 * scale_factor)
    t.fillcolor('alice blue')
    t.begin_fill()
    draw_rectangle(t, 20 * scale_factor, 20 * scale_factor)
    t.end_fill()


def create_tractor(t, scale_factor = 1.0, main_color = 'green'):
    # Main box
    reposition_turtle(t, -200 * scale_factor, 0 * scale_factor)
    t.fillcolor(main_color)
    t.begin_fill()
    draw_rectangle(t, 50 * scale_factor, 100 * scale_factor)
    t.end_fill()
    # Cabin
    reposition_turtle(t, -140 * scale_factor, 50 * scale_factor)
    t.begin_fill()
    draw_rectangle(t, 40 * scale_factor, 40 * scale_factor)
    t.end_fill()
    reposition_turtle(t, -135 * scale_factor, 55 * scale_factor)
    t.fillcolor('alice blue')
    t.begin_fill()
    draw_rectangle(t, 30 * scale_factor, 15 * scale_factor)
    t.end_fill()
    reposition_turtle(t, -145 * scale_factor, 90 * scale_factor)
    t.fillcolor('silver')
    t.begin_fill()
    draw_rectangle(t, 5 * scale_factor, 50 * scale_factor)
    t.end_fill()
    # Spout
    reposition_turtle(t, -190 * scale_factor, 50 * scale_factor)
    t.begin_fill()
    draw_rectangle(t, 30 * scale_factor, 10 * scale_factor)
    t.end_fill()
    # Wheels
    reposition_turtle(t, -190 * scale_factor, -15 * scale_factor)
    t.fillcolor('black')
    t.begin_fill()
    draw_circle(t, 25 * scale_factor)
    t.end_fill()
    reposition_turtle(t, -120 * scale_factor, -15 * scale_factor)
    t.begin_fill()
    draw_circle(t, 30 * scale_factor)
    t.end_fill()
    reposition_turtle(t, -190 * scale_factor, -3 * scale_factor)
    t.fillcolor('yellow')
    t.begin_fill()
    draw_circle(t, 12.5 * scale_factor)
    t.end_fill()
    reposition_turtle(t, -120 * scale_factor, -3 * scale_factor)
    t.begin_fill()
    draw_circle(t, 17 * scale_factor)
    t.end_fill()


def draw_rectangle(t, height, width):
    for i in range(2):
        t.forward(width)
        t.lt(90)
        t.forward(height)
        t.lt(90)


def draw_triangle(t, length, angle):
    for i in range(3):
        t.lt(angle)
        t.forward(length)


def draw_circle(t, radius):
    t.circle(radius)


def reposition_turtle(t, x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()


if __name__ == "__main__":
    main()
    turtle.done()