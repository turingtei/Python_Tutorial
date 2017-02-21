'''
Challenge: Write a program that draws a polyline 
(an open polygon) based on a sequence of mouse clicks. 
The first click should create a point. Subsequent clicks 
should add a new segment to the polyline. 
You should include a “Clear” button that deletes the polyline
and restarts the drawing process.
'''

# Polyline drawing problem

###################################################
# Student should enter code below

try:
    import simplegui
except:
    import simpleguitk as simplegui

import math

polyline = []


# define mouseclick handler
def click(pos):
  polyline.append(pos)
  print (polyline)
# button to clear canvas
def clear():
  global polyline
  polyline = []
# define draw
def draw(canvas):
  #canvas.draw_point(
  if len(polyline) == 1:
    canvas.draw_circle([polyline[0][0],polyline[0][1]],1,1,'Yellow','Yellow')
  elif len(polyline) > 1:
    canvas.draw_polyline(polyline,1,'Yellow')
    
  pass                 
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 500, 200,600)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear,100)

# start frame
frame.start()


