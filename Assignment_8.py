'''
Jon Zheng
This program is designed to take in the coordiantes of the inner most corner of the shape then the gap and number and sequences to draw a spiraling
shape until the desired amount of sequences is hit. The turtle will not show.
'''
import turtle

# Easy coding
t = turtle

# Input for the X, Y coordinates
x_coor = int(input('Enter x coordinate of inner-most corner: '))
y_coor = int(input('Enter y coordinate of inner-most corner: '))

# Input for the gap between the parallel lines
gap = int(input('Enter the gap between two adjacent parallel lines: '))

# Gives error message if gap is less than 5
if gap < 5:
    print('Gap should be at least 5')

# Continues the program if condition is met
else:
    num_seq = int(input('Enter the number of sequences: '))
    
    # Gives error message if the number of sequences is less than 2
    if num_seq < 2:
        print('Number of sequences must be at least 2')
    
    # Continues the program if condition is met    
    else:
        side_len = gap # gives the length of the side for turtle to draw
        t.hideturtle() 
        t.penup() 
        t.goto(x_coor,y_coor)
        t.pendown()
        t.speed(11) # Speeds up the program
        
        
        for x in range(num_seq):
            t.forward(side_len)
            t.right(90)
            t.forward(side_len)
            t.right(90)
            side_len += gap # creates new variable for rest of program
            t.forward(side_len)
            t.right(90)
            t.forward(side_len)
            t.right(90)
            side_len += gap # updates the length for new loop
            
        t.done()