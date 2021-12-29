import turtle
import random

# pencolor(pen_color) = choose the color of pen
# fillcolor(fill_color) = slect the color to fill
# begin_fill() = start to color turtle
# end_fill() = stop filling 
# goto(x,y) = turtle moves the position x, y
# penup() = lift pen up, lifting pen will not make mark in screen
# pendown() = touch the pen to the board, it left mark in board

global isTree
isTree = True

# function draw the triangle in the position centre_x, centre_y with the width, height,
# pen_color, and fill_color to fill the triangle
def draw_triangle(centre_x, centre_y, width, height, pen_color, fill_color):

    save_state(centre_x, centre_y, pen_color, fill_color)

    # for loop runs 3 times to make triangle 3 times stacking one another
    for a in range(3):
        width = width
        rec_width = 15
        tri_height = height
        height_increase = (60/100)* height #go 60% height of the triangle so next turtle cover 40% of previous triangle

        # x_init, y_init takes the value of current x, y value respectively
        # middle is the middle the of the branch(rectangle)
        # x_bottom_right, x_bottom_left, and y_top are the point where the triangle edge will be
        x_init, y_init = (turtle.xcor(), turtle.ycor())
        middle = x_init + rec_width/2
        x_bottom_left = x_init - width/2
        x_bottom_right = x_init + width/2 + rec_width
        y_top = y_init + tri_height
        turtle.pencolor(pen_color)  
        turtle.fillcolor(fill_color) 
        turtle.begin_fill()         

        turtle.goto(x_bottom_left, y_init)
        turtle.goto(middle, y_top)
        turtle.goto(x_bottom_right, y_init)
        turtle.goto(x_init, y_init)
        turtle.sety(turtle.ycor() + height_increase)
        turtle.end_fill()
    
    restore_state(centre_x, centre_y, pen_color, fill_color)

# will draw a rectangle(steam) in the position centre_x, centre_y, with dimension width and height
# pen_color = outline of rectnagle
# fill_color = color of filling
def draw_rectangle(centre_x, centre_y, width, height, pen_color, fill_color):
    save_state(centre_x, centre_y, pen_color, fill_color)
    turtle.penup()
    turtle.goto(centre_x, centre_y)
    turtle.pendown()
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()

    for a in range(2):
        # forward() = turtle moves specific distance (width) to the east
        # Note = turtle face to east initially
        turtle.forward(width)   
        turtle.right(90)    # face turtle 90 to initial position
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

    restore_state(centre_x, centre_y, pen_color, fill_color)

# draw the circle in the position centre_x, centre_y, with radidus = radius,
# isTree is a boolean variable to check wheather circle is filled with color or not
def draw_circle(centre_x, centre_y, radius, pen_color, fill_color, isTree):
    tree_circle_x, tree_circle_y = (centre_x, centre_y) # tree circle position
    bird_circle_x, bird_circle_y = (centre_x + 100, centre_y) # Bird circle position
    save_state(centre_x, centre_y, pen_color, fill_color)

    # draws the 1st circle for the Tree selector
    turtle.pencolor(pen_color)
    turtle.penup()
    turtle.goto(tree_circle_x, tree_circle_y)
    turtle.fillcolor(fill_color)
    turtle.pendown()
    if (isTree == True):
        turtle.begin_fill()
    turtle.circle(radius)
    turtle.penup()
    turtle.end_fill()
    turtle.goto(15,370)
    turtle.pendown()
    turtle.write('Tree') # write the text 'Tree' next to 1st circle

    # draws the 2st circle for the Bird selector
    turtle.pencolor(pen_color)
    turtle.penup()
    turtle.goto(bird_circle_x, bird_circle_y)
    turtle.fillcolor(fill_color)
    turtle.pendown()
    if(isTree != True):
        turtle.begin_fill()
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(115,370)
    turtle.write('Bird') # write the text 'Bird' next to 2st circle

    restore_state(centre_x, centre_y, pen_color, fill_color)

# draw to outline of canvas 
def inner_rectangle(inner_rec_width, inner_rec_height):
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(-350,350) # to the position top left of inner rectangle
    turtle.pendown()
    for a in range(4):
        turtle.forward(inner_rec_height)
        turtle.right(90)
    turtle.pensize(1)
    
# function stamp_turtle(entre_x, centre_y, color) copy the current turtle and past into the position centre_x and centre_y
def stamp_turtle(centre_x, centre_y, color):
    save_state(centre_x, centre_y, pen_color='#810082', fill_color='#810082')
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(centre_x,centre_y)
    turtle.stamp()

    restore_state(centre_x, centre_y, pen_color, fill_color)

def distance(x1, y1, x2, y2):
    print('distance')

def save_state(x,y,pen_color,fill_color):
    x,y = (x,y)
    pen_color = pen_color
    fill_color = fill_color    

def restore_state(x,y,pen_color,fill_color):
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(x,y)
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)


# function will hanldle the mouse click nd key press
def handle_click(x, y):
    print('detected click at ',x,y)
    # condinates of 1st circle
    # entre the condtion if the mouse click (x,y) is inside the 1st circle
    if (x >= -10 and x <= 10 and y>=370 and y<=390):
        global isTree
        isTree = True
        # overlapp the circle and make isTee = True
        draw_circle(centre_x=0, centre_y=370, radius= 10, pen_color='black', fill_color='green', isTree = True)
    
    # entre the condtion if the mouse click (x,y) is inside the 2nd circle
    elif(x >= 90 ) and (x <= 110) and (y>=370) and (y<=390):
        
        isTree = False
        # overlap the circle and make isTree = False
        draw_circle(centre_x=0, centre_y=370, radius= 10, pen_color='black', fill_color='green', isTree = False)
        turtle.penup()
        turtle.pencolor('#810082')  # Bird outline color
        turtle.fillcolor('#810082') # Bird color
        turtle.goto(-340, 370) # position where Bird is made
        turtle.hideturtle()
        turtle.pendown()
        turtle.begin_fill()

        # register the shape and give the name Bird to the shape
        turtle.register_shape('bird', ((-22,-39),(-20,-7),(-7,3),(-11,7),(-12,9),(-11,10),(-9,10),(-3,7),
        (10,24),(30,16),(13,18),(4,0),(14,-6),(6,-13),(0,-4),(-14,-13),(-22,-39)))
        turtle.shape('bird')
        turtle.end_fill()
        turtle.stamp() # make bird 

    # condition for the mouse click
    # check is the mouse click is inside the inner rectangle and Tree is seclected or not
    # if Tree is selected i.e. isTree = True draw the tree inside the inner rectanle in the position x,y
    # else draw bird in postion x, y
    if(x >= -350 and x <= 350 and y >= -350 and y <= 350) and isTree == True:
        # scaleFacor to scale tree by number
        # random.uniform(0.7, 1.3) = returns random float number between 0.7 - 1.3
        scaleFactor = random.uniform(0.7, 1.3)
        draw_rectangle(x,y,15*scaleFactor,80*scaleFactor,'brown','brown')
        draw_triangle(x,y,100*scaleFactor,50*scaleFactor,'green','green')
    
    elif(x >= -350 and x <= 350 and y >= -350 and y <= 350) and isTree != True:
        stamp_turtle(x,y,color='#810082')

# function left_keypress() will tilt the turtle by the angle 20
def left_keypress():
    turtle.tiltangle(20) # tilt the turtle by the angle 20

def right_keypress():
    turtle.tiltangle(-20) # tilt the turtle by the angle negative 20