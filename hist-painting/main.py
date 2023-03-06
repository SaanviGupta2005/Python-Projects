# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)


import turtle as turtle_module
import random

color_list = [(145, 91, 40), (140, 26, 49), (151, 107, 105), (132, 177, 203), (158, 158,158), (145, 55, 104),
              (169, 160, 39), (129, 189, 143), (83, 20, 44), (137, 78, 174), (186, 94, 107), (169,169,169),
              (85, 120, 180), (169, 89, 31), (188,188,188), (78, 153, 165), (194, 79, 73), (145,145,145), (154,154,154),
              (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]
tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
