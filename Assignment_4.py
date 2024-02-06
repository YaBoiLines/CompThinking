'''
Jon Zheng
This program is design to take input from the user in regards to the size of the rectangular box and how many people chose a certain color.
It will then create a bar graph displaying the information in the appropriate colors.

Pseudocode
Read the width of the rectangle as rec_width
Read the height of the rectangle as rec_height
Read in the number of people who pick red as red_people
Read in the number of people who pick green as green_people
Read in the number of people who pick blue as blue_people
Read in the number of people who pick orange as orange_people

Set bar_width = rec_width * 0.2
Set emp_space = (0.2 / 3) * rec_width
Set total_people = red_people + green_people + blue_people + orange_people
Set red_bar = (red_people / total_people) * rec_height
set green_bar = (green_people / total_people) * rec_height
set blue_bar = (blue_people / total_people) * rec_height
set orange_bar = (orange_people / total_people) * rec_height
set red_coor = (0,0)
set green_coor = ((bar_width + emp_space),0)
set blue_coor = (((2 * bar_width) + (2 * emp_space)), 0)
set orange_coor = (((3  * bar_width) + (3 * emp_space)), 0)

Simplify turtle input as t

Create the rectangular box using rec_width and rec_height as parameters for size of the box

Each bar for red, green, blue, orange.
    1. Reset turtle start position to corresponding color coordinate
    2. put the pen down
    3. Reset heading to 0
    4. Set pencolor to corresponding color
    5. Set Fillcolor to corresponding color
    6. Begin filling
    7. Go forward bar_width
    8. change directions 90 degrees left
    9. Go forward corresponding barcolor height
    10. change direction 90 degrees left
    11. go forward bar_width
    12. write the variable of how many people chose the corresponding color
    13. change direction 90 degrees left
    14. go forward corresponding barcolor height
    15. end filling
    16. put pen up
    
When all bars are down end program.

'''

import turtle

# Big Box dimensions
rec_width = float(input('Enter rectangle width: '))
rec_height = float(input('Enter rectangle height: '))

# Input for people choosing colors
red_people = int(input('Enter number of people who picked red: '))
green_people = int(input('Enter number of people who pick green: '))
blue_people = int(input('Enter number of people who pick blue: '))
orange_people = int(input('Enter the number of people who pick orange: '))

# Equation for space in Big Box
bar_width = rec_width * 0.2
emp_space = (0.2 /3) *rec_width

# Equation for total amount of people
total_people = red_people + green_people + blue_people + orange_people

# Calculation far the height of each bar
red_bar = (red_people / total_people) * rec_height
green_bar = (green_people / total_people) * rec_height
blue_bar = (blue_people / total_people) * rec_height
orange_bar = (orange_people / total_people) * rec_height

# Coordinates for next bars
red_coor = (0,0)
green_coor = ((bar_width + emp_space),0)
blue_coor = (((2 * bar_width) + (2 * emp_space)), 0)
orange_coor = (((3  * bar_width) + (3 * emp_space)), 0)

# Easier coding
t = turtle

# Big Box
t.pendown()
t.hideturtle()
t.forward(rec_width)
t.left(90)
t.forward(rec_height)
t.left(90)
t.forward(rec_width)
t.left(90)
t.forward(rec_height)

# Red bar
t.goto(0,0)
t.pendown
t.setheading(0)
t.pencolor('red')
t.color('red')
t.begin_fill()
t.forward(bar_width)
t.left(90)
t.forward(red_bar)
t.left(90)
t.forward(bar_width)
t.write(red_people)
t.left(90)
t.forward(red_bar)
t.end_fill()
t.penup()

# Green Bar
t.goto(green_coor)
t.pendown
t.setheading(0)
t.pencolor('green')
t.color('green')
t.begin_fill()
t.forward(bar_width)
t.left(90)
t.forward(green_bar)
t.left(90)
t.forward(bar_width)
t.write(green_people)
t.left(90)
t.forward(green_bar)
t.end_fill()

#Blue Bar
t.goto(blue_coor)
t.pendown
t.setheading(0)
t.pencolor('blue')
t.color('blue')
t.begin_fill()
t.forward(bar_width)
t.left(90)
t.forward(blue_bar)
t.left(90)
t.forward(bar_width)
t.write(blue_people)
t.left(90)
t.forward(blue_bar)
t.end_fill()

#Orange Bar
t.goto(orange_coor)
t.pendown
t.setheading(0)
t.pencolor('orange')
t.color('orange')
t.begin_fill()
t.forward(bar_width)
t.left(90)
t.forward(orange_bar)
t.left(90)
t.forward(bar_width)
t.write(orange_people)
t.left(90)
t.forward(orange_bar)
t.end_fill()

t.done()