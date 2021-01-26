import turtle
from random import choice
from turtle import Turtle, Screen

import colorgram
# Using colorgram package extract color palette from an image, create a list containing tuples of which each
# contains 3 numbers representing the RGB color values.


def return_color_palette(image, number_of_colors):
    """
    Returns a list containing tuple data structures, each representing a RGB color value.
    :param image: Image location/ path, passed  in as string.
    :param number_of_colors: Integer, representing number of colors to be extracted from the image.
    :return: List of tuples, each containing three values.
    """
    color_palette = colorgram.extract(image, number_of_colors)  # print(color_palette)  # returns a Color Object.
    tuple_rgb_data = []
    for index in range(len(color_palette)):
        rgb_element = color_palette[index].rgb
        # print(rgb_element)  # prints a named tuple containing three values.
        # (named tuple is similar to JS objects by appearance and functionality).
        tuple_rgb_data.append((rgb_element.r, rgb_element[1], rgb_element[2]))
    return tuple_rgb_data


print(choice(return_color_palette("./Images/hirst_dots.jpg", 10)))


canvas = Screen()
canvas.setup(width=.50, height=.75, startx=None, starty=None)  # sets the width and height of canvas depending on
# view port resolution and centers it to the middle of view port.
turtle.colormode(255)

dot_brush = Turtle()
dot_brush.shape("classic")
dot_brush.speed(7)
move = 20

for _ in range(move):
    dot_brush.penup()
    dot_brush.fd(20)
    dot_brush.dot(20, choice(return_color_palette("./Images/hirst_dots.jpg", 10)))
    # could use turtle.dot(size_of_dot, color_of_dot) function but it seems resolution of dot is
    # worse then using stamp() function.
    dot_brush.fd(20)


canvas.exitonclick()
