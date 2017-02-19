# template for "Stopwatch: The Game"
'''Mini-project description - "Stopwatch: The Game"

Our mini-project for this week will focus on combining text drawing in the canvas with timers to build a simple digital stopwatch that keeps track of the time in tenths of a second. The stopwatch should contain "Start", "Stop" and "Reset" buttons. To help guide you through this project, we suggest that you download the provided program template for this mini-project and build your stopwatch program as follows:

Mini-project development process

Construct a timer with an associated interval of 0.1 seconds whose event handler increments a global integer. (Remember that 𝚌𝚛𝚎𝚊𝚝𝚎_𝚝𝚒𝚖𝚎𝚛 takes the interval specified in milliseconds.) This integer will keep track of the time in tenths of seconds. Test your timer by printing this global integer to the console. Use the CodeSkulptor reset button in the blue menu bar to terminate your program and stop the timer and its print statements. Important: Do not use floating point numbers to keep track of tenths of a second! While it's certainly possible to get it working, the imprecision of floating point can make your life miserable. Use an integer instead, i.e., 12 represents 1.2 seconds.
Write the event handler function for the canvas that draws the current time (simply as an integer, you should not worry about formatting it yet) in the middle of the canvas. Remember that you will need to convert the current time into a string using 𝚜𝚝𝚛 before drawing it.
Add "Start" and "Stop" buttons whose event handlers start and stop the timer. Next, add a "Reset" button that stops the timer and reset the current time to zero. The stopwatch should be stopped when the frame opens.
Next, write a helper function 𝚏𝚘𝚛𝚖𝚊𝚝(𝚝) that returns a string of the form 𝙰:𝙱𝙲.𝙳 where 𝙰, 𝙲 and 𝙳 are digits in the range 0-9 and 𝙱 is in the range 0-5. Test this function independent of your project using this testing template http://www.codeskulptor.org/#examples-format_template.py. (Just cut and paste your definition of 𝚏𝚘𝚛𝚖𝚊𝚝 into the template.) Note that the string returned by your helper function 𝚏𝚘𝚛𝚖𝚊𝚝 should always correctly include leading zeros. For example: 𝚏𝚘𝚛𝚖𝚊𝚝(𝟶) = 𝟶:𝟶𝟶.𝟶 , 𝚏𝚘𝚛𝚖𝚊𝚝(𝟷𝟷) = 𝟶:𝟶𝟷.𝟷 , 𝚏𝚘𝚛𝚖𝚊𝚝(𝟹𝟸𝟷) = 𝟶:𝟹𝟸.𝟷 , and 𝚏𝚘𝚛𝚖𝚊𝚝(𝟼𝟷𝟹) = 𝟷:𝟶𝟷.𝟹 .
Insert a call to the 𝚏𝚘𝚛𝚖𝚊𝚝 function into your draw handler to complete the stopwatch. (Note that the stopwatch need only work correctly up to 10 minutes, beyond that its behavior is your choice.)
Finally, to turn your stopwatch into a test of reflexes, add to two numerical counters that keep track of the number of times that you have stopped the watch and how many times you manage to stop the watch on a whole second (1.0, 2.0, 3.0, etc.). These counters should be drawn in the upper right-hand part of the stopwatch canvas in the form "𝚡/𝚢" where 𝚡 is the number of successful stops and 𝚢 is number of total stops. My best effort at this simple game is around a 25% success rate.
Add code to ensure that hitting the "Stop" button when the timer is already stopped does not change your score. We suggest that you add a global Boolean variable that is 𝚃𝚛𝚞𝚎 when the stopwatch is running and 𝙵𝚊𝚕𝚜𝚎 when the stopwatch is stopped. You can then use this value to determine whether to update the score when the "Stop" button is pressed.
Modify "Reset" so as to set these counters back to zero when clicked.
Steps 1-3 and 5-7 above are relatively straightforward. However, step 4 requires some adept use of integer division and modular arithmetic. So, we again emphasize that you build and debug the helper function 𝚏𝚘𝚛𝚖𝚊𝚝(𝚝) separately following the tips in the Code Clinic Tips page. Following this process will save you time. For an example of a full implementation, we suggest that you watch the video lecture on this mini-project.

Grading Rubric - 13 pts total (scaled to 100 pts)

1 pt - The program successfully opens a frame with the stopwatch stopped.
1 pt - The program has a working "Start" button that starts the timer.
1 pt - The program has a working "Stop" button that stops the timer.
1 pt - The program has a working "Reset" button that stops the timer (if running) and resets the timer to 0.
4 pts - The time is formatted according to the description in step 4 above. Award partial credit corresponding to 1 pt per correct digit. For example, a version that just draw tenths of seconds as a whole number should receive 1 pt. A version that draws the time with a correctly placed decimal point (but no leading zeros) only should receive 2 pts. A version that draws minutes, seconds and tenths of seconds but fails to always allocate two digits to seconds should receive 3 pts.
2 pts - The program correctly draws the number of successful stops at a whole second versus the total number of stops. Give one point for each number displayed. If the score is correctly reported as a percentage instead, give only one point.
2 pts - The "Stop" button correctly updates these success/attempts numbers. Give only one point if hitting the "Stop" button changes these numbers when the timer is already stopped.
1 pt - The "Reset" button clears the success/attempts numbers.


'''

# define global variables
try:
    import simplegui
except:
    import simpleguitk as simplegui

ticks = 0
width = 400
height = 400
first_time = True
first_try = True
stopwatch = '00:00.0'
points = 0
misses = 0
d = 0
score = 'Points(0)/Misses(0)'

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
	global d
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
	global first_try
	if first_time:
		timer.start()
		first_time = False
		first_try = True

def stop():
	timer.stop()
	global first_try
	global first_time
	first_time = True
	global points
	global misses
	global score
	if first_try:
		if d ==0:
			points+=1
			first_try = False
		else:
			misses+=1
			first_try = False
	
	score = 'Points(%d)/Misses(%d)' % (points,misses) 


def restart():
	global ticks
	global first_time
	global points
	global misses
	global score
	timer.stop()
	first_time = True
	ticks = 0
	points = 0
	misses = 0
	score = 'Points(0)/Misses(0)'

	format(ticks)


# define event handler for timer with 0.1 sec interval
def timer_handle():
	global ticks
	ticks +=1
	format(ticks)


# define draw handler
def draw_handler(canvas):
	canvas.draw_text(stopwatch,[height/2, width/2],30,'Yellow')
	canvas.draw_text(score, [100,40],20,'Red')

    
# create frame
frame = simplegui.create_frame("Stopwatch",width,height)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100,timer_handle)
start = frame.add_button("Start",start)
stop = frame.add_button("Stop", stop)
restart = frame.add_button("Restart", restart)


# register event handlers


# start frame
frame.start()


# Please remember to review the grading rubric
