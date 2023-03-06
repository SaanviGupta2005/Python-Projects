from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_counterclock():
    tim.left(10)


def move_clock():
    tim.right(10)


def clear_the_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counterclock)
screen.onkey(key="d", fun=move_clock)
screen.onkey(key="c", fun=clear_the_screen)
screen.exitonclick()
