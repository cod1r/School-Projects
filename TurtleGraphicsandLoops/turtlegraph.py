"""
A module to draw cool shapes with the Turtle module.

"""
import turtle

"""
TASK 1: Geometric drawing
"""

# This section creates a window with a turtle in it
window = turtle.Screen()  # Create window
window.bgcolor("black")  # Set the color of the window
window.title("Turtle Graphics")  # Set the title of the window
myShape = turtle.Turtle()  # Create turtle
myShape.pencolor("white")  # Set pen color
myShape.speed(2)  # Set speed to 2/10 so you can see what your turtle is doing in real time

# Create a star
for i in range(5):  # Loop repeats 5 times to reflect 5 sides of star
    myShape.forward(50)  # Distance the turtle will move
    myShape.right(144)  # Degrees the turtle will rotate before next movement

# Create a square
myShape.penup()  # Stop drawing
myShape.setpos(200, 200)  # Move the turtle
myShape.pendown()  # Resume drawing
for i in range(4):  # Loop repeats 4 times to reflect 4 sides of square
    # ***************************************#
    # Enter your code here. Hint: the turtle will need to turn 90 degrees.
    myShape.forward(100)  # Moves forward 100 units to make one side of the square
    myShape.right(90)  # turns the turtle 90 degrees
    # ***************************************#

# Create a a column of circles
myShape.penup()  # Stop drawing
myShape.setpos(-200, -200)  # Move the turtle
myShape.left(90)  # Rotate the turtle to face upwards (making a column, not a row)
myShape.pendown()  # Resume drawing
y = -200
for i in range(8):
    # ***************************************#
    # Enter your code here.
    myShape.circle(20)  # Creates a circle using the turtle
    y += 60  # moves the turtle 50 units up for another circle
    myShape.penup()  # stops drawing
    myShape.setposition(-200, y)
    myShape.pendown()  # resumes drawing
    # ***************************************#

myShape.clear()  # clears the window or Screen

"""
TASK 2: Circle
"""

# ***************************************#
# Enter your code here.
myShape.penup()  # stops drawing
myShape.setpos(-100, 100)  # sets the coordinates
myShape.pendown()  # resumes drawing
for i in range(360):
    myShape.right(1)  # turns turtle 1 degree
    myShape.forward(2.5)  # moves turtle one unit forward
# ***************************************#

myShape.clear()  # Resets the window.

"""
TASK 3: Shrinking lines
"""

# ***************************************#
# Enter your code here.
myShape.penup()  # stops drawing
length = 300  # how far the turtle will go up
width = 20  # how thick the pen will be
disX = -250  # how far apart each line will be
startx = -200  # how far apart the lines will be and the starting x pos of the turtle
starty = -100  # starting y pos of the turtle
for i in range(30):
    myShape.penup()  # stops drawing so the turtle won't leave a trail when relocating
    myShape.setpos(startx, starty)  # sets the position of the turtle
    myShape.pendown()  # starts drawing
    myShape.pensize(width)  # sets the pen size
    myShape.forward(length)  # moves turtle forward length units
    startx -= disX  # moves the turtle for the next line
    disX /= 2  # halves the distance of each line from each other
    starty += (length / 4)  # positions the y coordinate of the turtle after each iteration
    length /= 2  # halves how far the turtle will go
    width /= 2  # halves the thickness of the pen
# ***************************************#

myShape.clear()  # Resets the window.

"""
TASK 4: Equilateral triangles
"""

# ***************************************#
# Enter your code here.
myShape.penup()  # stops drawing
myShape.setpos(-100, -100)  # sets the position of the turtle for task 4
myShape.right(90)  # orients the turtle
ex = -100  # allows for the x value of the turtle to be changed
why = -100  # allows for the y value of the turtle to be changed
lengthsOfSide = 300  # allows for the length of each triangle to be proportionally changed
for i in range(3):
    for x in range(3):
        myShape.pendown()  # starts to draw a triangle
        myShape.forward(lengthsOfSide)  # moves the turtle forward with the pen
        myShape.left(120)  # turns the turtle left 120 degrees
    myShape.penup()  # stop the drawing
    lengthsOfSide *= 2 / 3  # changes the length of the side
    ex += lengthsOfSide / 4  # relocates the x position of the turtle by a fourth of the length of the side
    why += 20  # adds 20 units to the y value of the turtle
    myShape.setpos(ex, why)  # officially sets the turtle at the position
# ***************************************#

turtle.done()  # Program is finished.
