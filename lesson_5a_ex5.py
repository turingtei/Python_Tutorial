'''
Complete the given program template to produce a program
that fills the canvas with a 10x10 grid of touching balls
of the given size. You should use two 'for' loops, one nested
inside the other, placed in the draw handler.
'''
# Ball grid slution

###################################################
# Student should enter code below

try:
    import simplegui
except:
    import simpleguitk as simplegui

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS


# define draw
def draw(canvas):
  for i in range(10):
    for j in range(20,420,40):
      canvas.draw_circle([j,HEIGHT/2],BALL_RADIUS,1,'Yellow','Yellow')
                      
# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()

