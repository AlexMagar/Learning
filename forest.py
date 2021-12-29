import turtle
import utilities
# window_width and window_height is 800*800, is turtle window size 
# inner rectangle size is 700*700
#
if __name__ =="__main__":
    window_width = 800; window_height = 800
    inner_rec_width, inner_rec_height = (700,700) 
    turtle.setup(window_width, window_height)

    #speed of turtle where
    # 0 = fastest
    # 10 = fast
    # 1 = slowest
    turtle.speed(0)
    turtle.bgcolor('#fee3c3') #background color of turtle screen
    turtle.hideturtle()     #hidding the turtle icon
    utilities.inner_rectangle(700,700)
    #function draw_circle call from the module utilities.py
    utilities.draw_circle(centre_x=0, centre_y=370, radius= 10, pen_color='black', fill_color='green', isTree=True)
    turtle.speed(10)
    turtle.listen() #listening to mouse and key event

    #call the function hande_click() if the left mouse is clicked
    # 1 = left mouse
    # 2 = middle mouse
    # 3 = right mouse
    turtle.onscreenclick(utilities.handle_click, 1)

    # call the function left_keypress and right_keypress when Left and Right
    # button is pressed respectively
    turtle.onkey(utilities.left_keypress, 'Left')
    turtle.onkey(utilities.right_keypress, 'Right')

    turtle.done() #stop turtle screen from closing