#Collisions and Reflection

'''
Pair of points on a canvas p,q

store as a list 
first component is the horizontal
second comonent is the vertical
[p[0],p[1],[q[0],q[0]]

Compute Distance Between 2 points

Pythagorean Formula
dist(p,q)^2 = (p[0]-q[0])^2 + (p[1]-q[1])^2

def dist(p,q):
  return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

Vectors and Motion
Vector as difference of two points
v = p-q
v[0] = p[0] - q[0]
v[1] = p[1] - q[1]

Move/Translate a point using a vector
p = q + v

p[0] = q[0] + v[0]
p[1] = q[1] + v[1]

Update for motion
point at position 'p' with velociti 'v' and constant 'a'

p = p + a * v

p[0]=p[0]+a*v[0]
p[1]=p[1]+a*v[1]

Collisions
  of point 'p' with wall
  left wall
    p[0] <= 0
  right wall
    p[0] >= width
  of a ball wihth radius 'r' and center 'p' with the wall
    left wall
      p[0] <= r
    right wall
      p[0] >= width - r
Reflections

Motion update
p[0]=p[0]+a*v[0]
p[1]=p[1]+a*v[1]

Reflections - update the velocity vector 'v'

Left Wall - compute reflected velocity vector
v[0] = -v[0]
v[1] = v[1]
'''

try:
    import simplegui
except:
    import simpleguitk as simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-40.0 / 60.0,  5.0 / 60.0]

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = - vel[0]

    
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
