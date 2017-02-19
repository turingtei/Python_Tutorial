# template for "Stopwatch: The Game"


# define global variables
try:
    import simplegui
except:
    import simpleguitk as simplegui

ticks = 0
width = 400
height = 400
first_time = True
stopwatch = '00:00.0'

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t//600
    t = t-a*600
    b = t//100
    t = t-b*100
    c = t//10
    t = t-c*10
    d = t
    global stopwatch
    if a<10:

    	stopwatch = ("0%d:%d%d.%d") % (a,b,c,d)
    else:
    	stopwatch = ("%d:%d%d.%d") % (a,b,c,d)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
	global first_time
	if first_time:
		timer.start()
		first_time = False

def stop():
	timer.stop()

def restart():
	global ticks
	global first_time
	timer.stop()
	first_time = True
	ticks = 0
	format(ticks)


# define event handler for timer with 0.1 sec interval
def timer_handle():
	global ticks
	ticks +=1
	format(ticks)


# define draw handler
def draw_handler(canvas):
	canvas.draw_text(stopwatch,[height/2, width/2],30,'Yellow')

    
# create frame
frame = simplegui.create_frame("Stopwatch",width,height)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(10,timer_handle)
start = frame.add_button("Start",start)
stop = frame.add_button("Stop", stop)
restart = frame.add_button("Restart", restart)


# register event handlers


# start frame
frame.start()


# Please remember to review the grading rubric
