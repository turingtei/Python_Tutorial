#For each mouse click, print the position of the mouse
#click to the console.

# Echo mouse click in console

###################################################
# Student should enter code below
try:
    import simplegui
except:
    import simpleguitk as simplegui
x = 0
y = 0
ballColor = "Black"

def mouseClick(position):
  print ('Mouse click at', position)
  global x,y,ballColor

  x = position[0]
  y = position[1]
  ballColor = "Red"
def drawHandler(canvas):
  global x,y
  canvas.draw_circle((x,y),20,1,ballColor,ballColor)


f = simplegui.create_frame("Mouse Clicks",400,400,)
f.set_draw_handler(drawHandler)
f.set_mouseclick_handler(mouseClick)

f.start()


###################################################
# Sample output

#Mouse click at (104, 105)
#Mouse click at (169, 175)
#Mouse click at (197, 135)
#Mouse click at (176, 111)
#Mouse click at (121, 101)
#Mouse click at (166, 208)
#Mouse click at (257, 235)
#Mouse click at (255, 235)