# Implementation of classic arcade game Pong
# Play pong

try:
    import simplegui
except:
    import simpleguitk as simplegui

import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2,HEIGHT / 2]
ball_vel = [0,0]


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as list
    if direction == LEFT:
        ball_vel = [random.randrange(-4,-1),random.randrange(-3,-1)]
    if direction == RIGHT:
        ball_vel = [random.randrange(1,4),random.randrange(-3,-1)]
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2

    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0

    #randomize starting vector
    starting = random.randrange(1,3)
    if starting == 1:
        spawn_ball(RIGHT)
    elif starting == 2:
        spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[0] < BALL_RADIUS+PAD_WIDTH:
        if (paddle1_pos + HALF_PAD_HEIGHT) > ball_pos[1] and (paddle1_pos - HALF_PAD_HEIGHT) < ball_pos[1]:
            ball_vel[0] = -ball_vel[0]
            ball_vel[1] = -ball_vel[1]

        else:
            ball_pos = [WIDTH/2,HEIGHT/2]
            ball_vel = [random.randrange(1,4),random.randrange(-3,-1)]
            score2+=1
        
    elif ball_pos[0] > (WIDTH - BALL_RADIUS - PAD_WIDTH):
        if (paddle2_pos + HALF_PAD_HEIGHT) > ball_pos[1] and (paddle2_pos - HALF_PAD_HEIGHT) < ball_pos[1]:
            ball_vel[0] = -ball_vel[0]
            ball_vel[1] = -ball_vel[1]

        else:
            ball_pos = [WIDTH / 2,HEIGHT / 2]
            ball_vel = [random.randrange(1,4),random.randrange(-3,-1)]
            score1+=1
        
    if ball_pos[1] < BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] > (HEIGHT - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,1,'Red','Red')
    
    # update paddle's vertical position, keep paddle on the screen
    if ((paddle1_pos + paddle1_vel) >= (HALF_PAD_HEIGHT)) and ((paddle1_pos + paddle1_vel) <= (HEIGHT - HALF_PAD_HEIGHT)):
        paddle1_pos += paddle1_vel

    if ((paddle2_pos + paddle2_vel) >= (HALF_PAD_HEIGHT)) and ((paddle2_pos + paddle2_vel) <= (HEIGHT - HALF_PAD_HEIGHT)):
        paddle2_pos += paddle2_vel
    

    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos + HALF_PAD_HEIGHT], [PAD_WIDTH,paddle1_pos + HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [0, paddle1_pos - HALF_PAD_HEIGHT]], 1, 'Yellow', 'Yellow')
    canvas.draw_polygon([[WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH,paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos - HALF_PAD_HEIGHT]], 1, 'Blue', 'Blue')
    
    # determine whether paddle and ball collide
    #if (paddle2_pos+HALF_PAD_HEIGHT)>ball_pos[1] and (paddle2_pos-HALF_PAD_HEIGHT)<ball_pos[1]:

    # draw scores
    canvas.draw_text(str(score1), ((WIDTH / 2) - 40, 50), 40, 'Yellow')
    canvas.draw_text(str(score2), ((WIDTH / 2) + 40, 50), 40, 'Blue')    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 4

    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

def restart():
    new_game()


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restartButton = frame.add_button('Restart', restart,100)

new_game()
frame.start()
print ('status: frame.start()')


# start frame
#new_game()
#frame.start()
