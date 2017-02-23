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
half_width = 50/2
half_height = 100/2
letter_height = 75
list_numbers=[]
letter_center = []



# helper function to initialize globals
def new_game():
  global list_numbers, center_cards
  for i in range(8):
    list_numbers.append(i)
  list_numbers+=list_numbers
  random.shuffle(list_numbers)

  #print("list_numbers length",len(list_numbers))

  for i in range(25,801,50):
    center_cards.append([i,half_height])

  for i in range(10,801,50):
    letter_center.append([i,letter_height])
  #print("center_cards length",len(center_cards))
     
# define event handlers
def mouseclick(pos):
  # add game state logic here
  pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
  pass
  #center of the cards

  #print (len(center_cards))
  for j in center_cards:
    canvas.draw_polygon([[(j[0]-half_width),(j[1]-half_height)], [(j[0]+half_width),(j[1]-half_height)], [(j[0]+half_width),(j[1]+half_height)], [(j[0]-half_width),(j[1]+half_height)]], 1, 'White', 'Blue')
  for k in range(len(list_numbers)):
    canvas.draw_text(str(list_numbers[k]),letter_center[k],50,"Red")



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