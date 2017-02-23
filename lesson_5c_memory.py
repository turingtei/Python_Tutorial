# implementation of card game - Memory

try:
    import simplegui
except:
    import simpleguitk as simplegui
import random

card_width = 50
card_height = 100
canvas_width = 800
center_cards=[]


# helper function to initialize globals
def new_game():
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
  #center of the cards
  global center_cards
  for i in range(25,801,50):





# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric