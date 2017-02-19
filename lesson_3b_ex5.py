'''Use a timer to measure how fast you can press a button twice.
Create a button that starts a timer that ticks every hundredth of a
second. The first button press starts the measurement. The second
button press ends the measurement. Print to the console the time
elapsed between button presses. The next two button presses should
repeat this process, making a new measurement. Hint: We suggest that
you keep track of whether the program is on the first or second button
press using a global Boolean variable.'''

try:
    import simplegui
except:
    import simpleguitk as simplegui

 # Reflex tester

###################################################
# Student should add code where relevant to the following.

total_ticks = 0
first_click = True


# Timer handler
def tick():
    global total_ticks
    total_ticks+=1

    
# Button handler
def click():
    global first_click, total_ticks
    if first_click:
        timer.start()
        first_click = False

    else:
        timer.stop()
        print("Stopped. reflex %d ") % total_ticks
        total_ticks = 0
        first_click = True




# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()

