import random
from turtle import Turtle, Screen

game_on=True
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


tim = Turtle(shape="turtle")
tim.color(colors[0])
tim.penup()
tim.goto(x=-230, y=-10)
while game_on:
    tim.forward(random.randint(0, 10))

tom = Turtle(shape="turtle")
tom.color(colors[1])
tom.penup()
tom.goto(x=-230, y=20)
while game_on:
    tom.forward(random.randint(0, 10))

nin = Turtle(shape="turtle")
nin.color(colors[2])
nin.penup()
nin.goto(x=-230, y=70)
while game_on:
    nin.forward(random.randint(0, 10))

benny = Turtle(shape="turtle")
benny.color(colors[3])
benny.penup()
benny.goto(x=-230, y=-70)
while game_on:
    benny.forward(random.randint(0, 10))

bun = Turtle(shape="turtle")
bun.color(colors[4])
bun.penup()
bun.goto(x=-230, y=-40)
while game_on:
    bun.forward(random.randint(0, 10))

jam = Turtle(shape="turtle")
jam.color(colors[5])
jam.penup()
jam.goto(x=-230, y=50)
while game_on:
    jam.forward(random.randint(0, 10))

screen.exitonclick()
