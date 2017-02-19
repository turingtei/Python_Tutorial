'''Given the solution from the following problem, 
we again want a counter printed to the console. 
Add three buttons that start, stop and reset the 
counter, respectively. '''

try:
    import simplegui
except:
    import simpleguitk as simplegui

# Counter with buttons

###################################################
# Student should add code where relevant to the following.

counter = 0

# Timer handler
def tick():
    global counter
    print (counter)
    counter += 1
    
# Event handlers for buttons    
def start_handler():
	timer.start()

def stop_handler():
	timer.stop()

def reset_handler():
	global counter
	timer.stop()
	counter = 0



        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(1000, tick)
start_button = frame.add_button('Start', start_handler)
stop_button = frame.add_button('Stop', stop_handler)
reset_button = frame.add_button('Reset',reset_handler)

frame.start()

# Start timer


