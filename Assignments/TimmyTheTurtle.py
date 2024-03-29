import turtle
import random



def main():
        t = turtle.Turtle()
        t.speed(0)  # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

        draw_circle(5, t)
        draw_square(5, t)
        draw_triangle(5, t)

def draw_circle(number_of_circles, t):
        # Random size of circle
        for i in range(number_of_circles):
                #Random size of circle
                radius = random.randint(10, 100)

                #Random position of circle
                x_pos = random.randint(-200, 200)
                y_pos = random.randint(-200, 200)
                t.penup()
                t.setposition(x_pos, y_pos)
                t.pendown()

                #Fill color of circle
                t.fillcolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
                t.begin_fill()

                # Create circle
                t.circle(radius)

                t.end_fill()


def draw_square(number_of_squares, t):
        number_of_squares_drawn = 0
        while number_of_squares_drawn < number_of_squares:
                #Random square size
                size = random.randint(20, 100)

                # Random position of squares
                x_pos = random.randint(-200, 200)
                y_pos = random.randint(-200, 200)
                t.penup()
                t.setposition(x_pos, y_pos)
                t.pendown()

                # Fill color of square
                t.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                t.begin_fill()

                # Draw square
                for i in range(4):
                        t.forward(size)
                        t.rt(90)

                t.end_fill()

                number_of_squares_drawn = number_of_squares_drawn + 1


def draw_triangle(number_of_triangles, t):
        number_of_triangles_drawn = 0
        while number_of_triangles_drawn < number_of_triangles:

                #Random size of triangle
                size = random.randint(20, 100)

                #Random position of triangles
                x_pos = random.randint(-200, 200)
                y_pos = random.randint(-200, 200)
                t.penup()
                t.setposition(x_pos, y_pos)
                t.pendown()

                #Random color of triangle
                t.fillcolor(random.randint(0, 255), random.randint(0,255), random.randint(0, 255))
                t.begin_fill()

                #Draw triangle
                for i in range(3):
                        t.forward(size)
                        t.rt(120)

                t.end_fill()

                number_of_triangles_drawn = number_of_triangles_drawn + 1

if __name__ == "__main__":
        main()