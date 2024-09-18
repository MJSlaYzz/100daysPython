###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
import random
# get the colors in the image
# rgb_colors = []
# colors = colorgram.extract("D:\\road_to_programing\GitHub\\100daysPython\hirstPaintingProject\\image.jpg", 30)
# for color in colors:
#     #rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

# by using https://www.w3schools.com/colors/colors_rgb.asp we can remove the first few color which are shades of white
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def my_way():
    tom = t.Turtle()
    tom.shape("circle")
    tom.pensize(20)
    tom.penup()
    t.colormode(255)
    for column in range(10):
        for row in range(10):
            tom.color(color_list[random.randint(0, len(color_list) - 1)])
            tom.stamp()
            tom.forward(50)
            #print(tom.pos())
            # print(tom.position()[1])
        tom.setx(0)
        tom.sety(tom.position()[1] + 50)

def her_way():
    tim = t.Turtle()
    t.colormode(255)
    tim.hideturtle()
    tim.penup()
    tim.setheading(225) #(270 + 180)/2 somewhere between the third quarter of the circle.
    tim.forward(300)
    tim.setheading(0)
    number_of_dots = 100
    tim.speed("fastest")
    for dot_count in range(1, number_of_dots + 1):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

her_way()


screen = t.Screen()
screen.exitonclick()




