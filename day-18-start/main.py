from turtle import Turtle, Screen
import random
import turtle as t

tim = Turtle()
# tim.shape("turtle")
tim.color("red")

# timmy_the_turtle.backward(50)
# for i in range(1, 5):
#     tim.forward(100)
#     tim.right(90)


# tim.pencolor("red")
# for i in range(15):
#     tim.forward(2)
#     tim.penup()
#     tim.forward(2)
#     tim.pendown()
#     tim.forward(2)


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)


t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# directions = [0, 90, 180, 270]
#
# tim.hideturtle()
# tim.pensize(10)
# tim.speed(10)
# for i in range(300):
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.pencolor(random_color())



tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(150)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(15)

screen = Screen()
screen.exitonclick()

