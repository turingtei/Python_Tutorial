#List Methods
'''
lst = [1,82,-6,4,3,8]
print (lst[2])  #-6
print (lst[-1]) #8

#in - check if something is in the list, returns True or False
#index - returns the location of the item in the list

print (82 in lst) #True or False
if 4 in lst:
  print ('4 is there')
print (lst.index(8))  #returns the location in the list of '8' -> 5

#append
#pop
lst[2] = 5

lst.append(632) #[1, 82, 5, 4, 3, 8, 632]
print (lst)
lst.pop()
print (lst)     #[1, 82, 5, 4, 3, 8]
lst.pop(4)
print (lst)     #[1, 82, 5, 4, 8]
'''

# Simple task list

try:
    import simplegui
except:
    import simpleguitk as simplegui

tasks = []

# Handler for button
def clear():
    global tasks
    tasks = []
    
# Handler for new task
def new(task):
    tasks.append(task)
    
# Handler for remove number
def remove_num(tasknum):
    n = int(tasknum)
    if n > 0 and n <= len(tasks):
        tasks.pop(n-1)

# Handler for remove name
def remove_name(taskname):
    if taskname in tasks:
        tasks.remove(taskname)
    #tasks.pop(tasks.index(taskname))
# Handler to draw on canvas
def draw(canvas):
    n = 1
    for task in tasks:
        pos = 30 * n
        canvas.draw_text(str(n) + ": " + task, [5, pos], 24, "White")
        n += 1
        
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Task List", 600, 400)
frame.add_input("New task:", new, 200)
frame.add_input("Remove task number:", remove_num, 200)
frame.add_input("Remove task:", remove_name, 200)
frame.add_button("Clear All", clear)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

