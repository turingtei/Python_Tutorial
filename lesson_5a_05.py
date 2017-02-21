# Examples of mouse input
#Remove balls from screen
try:
    import simplegui
except:
    import simpleguitk as simplegui

import math

# intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15
ball_color = "Red"

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    #you cannot take out indexes from a list that you are iterating
    #create a list of things you want to removed
    remove = []
    for ball in ball_list:
        if distance(ball, pos) < ball_radius:
            remove.append(ball)     #later on, remove this

    if remove == []:
        ball_list.append(pos)
    else:
        for ball in remove:
            ball_list.pop(ball_list.index(ball))
            #find the ball in the list and gets index position.
            #ball_list.pop removes the ball at that spot

def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0], ball[1]], ball_radius, 1, "Black", ball_color)
    
# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()
    