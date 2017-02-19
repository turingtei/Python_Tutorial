'''Math 

time(t)
velocity(v)
acceleration(a)
position(p)
p = v * t

Points and Vectors
x and y coordinate. Origin is upper left corner (0,0)

position and velocity changing with time:
p(t)
v(t)
p(t+1)=p(t)+(1)*(v(t))
p[0] = p[0]+v[0]
p[1] = p[1]+v[1]

Adding a vector to a points results in a new point.
Subtracting two points results in a vector

'''

# Ball motion with an explicit timer

try:
    import simplegui
except:
    import simpleguitk as simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

init_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 3]  # pixels per tick
time = 0

# define event handlers
def tick():
    global time
    time += 1

def draw(canvas):
    # create a list to hold ball position
    ball_pos = [0, 0]

    # calculate ball position
    ball_pos[0] = init_pos[0] + time * vel[0]
    ball_pos[1] = init_pos[1] + time * vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    canvas.draw_text(ball_pos, [100,100],12,'RED')

# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

timer = simplegui.create_timer(100, tick)
timer.start()

# start frame
frame.start()


