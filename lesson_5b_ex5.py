location = 'http://i.imgur.com/ghvJAC4.jpg'

try:
    import simplegui
except:
    import simpleguitk as simplegui

# global constants

# load test image
image = simplegui.load_image(location)
imWidth = image.get_width()
imHeight = image.get_height()
imCenterX = imWidth // 2
imCenterY = imHeight // 2


  
# draw handler
def draw(canvas):
  canvas.draw_image(image,(imCenterX,imCenterY),(imWidth,imHeight),(imCenterX,imCenterY),(imWidth,imHeight))

    
# create frame and register draw handler    
frame = simplegui.create_frame("Test image", imWidth, imHeight)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)


# start frame
frame.start()