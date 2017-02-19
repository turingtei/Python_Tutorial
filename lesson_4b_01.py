# control the position of a ball using the arrow keys
'''Positional control'''

try:
    import simplegui
except:
    import simpleguitk as simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
v = [0,0]       #velocity control

# define event handlers
def draw(canvas):
    ball_pos[0] += v[0]
    if ball_pos[0] < BALL_RADIUS:
        v[0] = -v[0]
    elif ball_pos[0] > (WIDTH-BALL_RADIUS):
        v[0] = -v[0]
    ball_pos[1] += v[1]
    if ball_pos[1] < BALL_RADIUS:
        v[1] = -v[1]
    elif ball_pos[1] > (HEIGHT -BALL_RADIUS):
        v[1] = -v[1]

    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

def keydown(key):
    acc = 4
    if key == simplegui.KEY_MAP["left"]:
        v[0] -= acc
    elif key == simplegui.KEY_MAP["right"]:
        v[0] += acc
    elif key == simplegui.KEY_MAP["down"]:
        v[1] += acc
    elif key == simplegui.KEY_MAP["up"]:
        v[1] -= acc        
    
# create frame 
frame = simplegui.create_frame("Positional ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
