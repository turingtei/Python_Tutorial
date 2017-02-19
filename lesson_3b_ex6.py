# template for "Stopwatch: The Game"
'''Construct a timer with an associated interval of 
0.1 seconds whose event handler increments a global integer.
(Remember that 𝚌𝚛𝚎𝚊𝚝𝚎_𝚝𝚒𝚖𝚎𝚛 takes the interval specified in milliseconds.)
This integer will keep track of the time in tenths of seconds.
Test your timer by printing this global integer to the console.
Use the CodeSkulptor reset button in the blue menu bar to terminate
your program and stop the timer and its print statements.
Important: Do not use floating point numbers to keep track of
tenths of a second! While it's certainly possible to get it working,
the imprecision of floating point can make your life miserable.
Use an integer instead, i.e., 12 represents 1.2 seconds.'''

# define global variables
try:
    import simplegui
except:
    import simpleguitk as simplegui

ticks = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
	timer.start()
def stop():
	timer.stop()
def restart():
	global ticks
	timer.stop()
	ticks = 0


# define event handler for timer with 0.1 sec interval
def timer_handle():
	global ticks
	ticks +=1


# define draw handler

    
# create frame
frame = simplegui.create_frame("Stopwatch",400,400)
timer = simplegui.create_timer(10,timer_handle)
start = frame.add_button("Start",start)
stop = frame.add_button("Stop", stop)
restart = frame.add_button("Restart", restart)


# register event handlers


# start frame
frame.start()


# Please remember to review the grading rubric
