#Jon Zheng

# Importing relevant commands
import turtle
import math

# Easier coding
t = turtle

# User inputs values for variables
x_coor = int(input('Enter x coordinate of top-left corner: '))
y_coor = int(input('Enter y coordinate of top-left corner: '))
square_side = float(input('Enter side of the largest square: '))
gap = float(input('Enter gap between squares: '))

# Creating large box
t.penup()
t.goto(x_coor - (2*square_side) ,y_coor)
t.pendown()
t.forward(square_side)
t.setheading(270)
t.forward(square_side)
t.setheading(180)
t.forward(square_side)
t.setheading(90)
t.forward(square_side)
t.penup()


if square_side >= 100:
    if gap < square_side:
        num_square = math.ceil(square_side/gap)
        for x in range(num_square):
                t.goto(x_coor - square_side, y_coor)
                t.pendown()
                t.setheading(180)
                t.forward (square_side) 
                t.setheading(270) 
                t.forward (square_side)
                t.penup()
                square_side -= gap
                x_coor -= gap
                y_coor -= gap
                
t.done()           
