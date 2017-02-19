'''
The program template contains a program designed to echo the
message "Presed Up arrow" or "Pressed down arrow" whenever
the appropriate key is pressed. Debug the program template
and fix the program.
'''

# Key board debugging - debug and fix the code below

try:
    import simplegui
except:
    import simpleguitk as simplegui

message = "Welcome!"

# Handler for keydown
def keydown(key):
    global message
    if key == simplegui.KEY_MAP["up"]:
        message = "Up arrow"
    elif key == simplegui.KEY_MAP["down"]:
        message = "Down arrow"
    return message

def keyup(key):
  pass

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
