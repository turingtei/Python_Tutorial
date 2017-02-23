'''
Load this image of an asteroid, and draw the image centered
at the last mouse click. Prior to any mouse clicks, the image
should be drawn in the middle of the canvas. The image size
is 95×93 pixels.
http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png

'''
# Image positioning problem

###################################################
# Student should enter code below

try:
    import simplegui
except:
    import simpleguitk as simplegui

# global constants
WIDTH = 400
HEIGHT = 300

# load test image
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png")
imWidth = image.get_width()
imHeight = image.get_height()
imCenterX = imWidth // 2
imCenterY = imHeight // 2
locationX = 0
locationY = 0

# mouseclick handler
def click(pos):
  global locationX,locationY
  locationX,locationY = pos


    
# draw handler
def draw(canvas):
  canvas.draw_image(image,(imCenterX,imCenterY),(imWidth,imHeight),(locationX,locationY),(imWidth,imHeight))

    
# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)


# start frame
frame.start()
        
                                       