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
letter_color = "Red"
state = 0
exposed = [False]*16
cards_index=list(range(0,16,1))
last = 0
second_to_last = 0
counter = 0



# helper function to initialize globals
def new_game():
  global list_numbers, center_cards, cards, state, counter, exposed
  list_number = []
  for i in range(8):
    list_numbers.append(i)
  list_numbers+=list_numbers
  random.shuffle(list_numbers)
  state = 0
  counter = 0
  exposed = [False]*16

  for i in range(25,801,50):
    center_cards.append([i,half_height])

  for i in range(10,801,50):
    letter_center.append([i,letter_height])

  #print("center_cards length",len(center_cards))
     
# define event handlers
def mouseclick(pos):
  # add game state logic here
  global clicked, exposed, state, last, second_to_last,counter

  if state == 0:
    second_to_last = pos[0]//50
    exposed[second_to_last] = True
    counter+=1
    state = 1
    
  elif state ==1:
    last = pos[0]//50
    if last !=second_to_last:
      exposed[last] = True
      counter+=1
      state = 2

  else:
    if list_numbers[last] == list_numbers[second_to_last]:
      exposed[last]=True
      exposed[second_to_last]=True
    else:
      exposed[last]=False
      exposed[second_to_last]=False
    
    second_to_last = pos[0]//50
    exposed[second_to_last]=True
    if second_to_last != last:
      counter+=1
    
    state = 1
  
    


  print (last)
  print (exposed)
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
  global exposed, letter_color

  for j in cards_index:
    if exposed[j] == False:
      canvas.draw_polygon([[(center_cards[j][0]-half_width),(center_cards[j][1]-half_height)], [(center_cards[j][0]+half_width),(center_cards[j][1]-half_height)], [(center_cards[j][0]+half_width),(center_cards[j][1]+half_height)], [(center_cards[j][0]-half_width),(center_cards[j][1]+half_height)]], 1, 'White', 'Blue')      
    #elif state[j] == 1:
    #  canvas.draw_text(str(list_numbers[j]),letter_center[j],50,letter_color)
    elif exposed[j] == True:
      canvas.draw_text(str(list_numbers[j]),letter_center[j],50,letter_color)
    canvas.draw_text(str(counter), (20, 20), 12, 'Red')



# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100,)
frame.set_canvas_background('Green')
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric