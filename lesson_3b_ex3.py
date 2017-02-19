'''Use a timer to toggle the canvas background back and forth 
between red and blue every 3 seconds. Use the CodeSkulptor Docs 
to locate the appropriate call to change the background color of 
the canvas.'''

try:
    import simplegui
except:
    import simpleguitk as simplegui

# Counter with buttons

###################################################
# Student should add code where relevant to the following.


color = "Red"


# Timer handler
def tick():
	global color
	if color == "Red":
		color = "Blue"
	else:
		color = "Red"
	frame.set_canvas_background(color)
	
        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.set_canvas_background(color)
timer = simplegui.create_timer(3000, tick)

# Start timer
frame.start()
timer.start()
