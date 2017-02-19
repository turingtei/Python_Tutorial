'''Create a circle in the center of the canvas. Use a timer to
increase its radius one pixel every tenth of a second. '''

try:
    import simplegui
except:
    import simpleguitk as simplegui

# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.

WIDTH = 200
HEIGHT = 200
radius = 1


# Timer handler
def time():
    global radius
    radius+=1

    
# Draw handler
def draw_handler(canvas):
    canvas.draw_circle((WIDTH/2,HEIGHT/2),radius, 10,"White","White")

        
# Create frame and timer
frame = simplegui.create_frame("Expanding Cirle", WIDTH, HEIGHT)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100,time)

# Start timer
frame.start()
timer.start()
