'''
Write a function day_to_number(day) that takes the supplied
global list day_list and returns the position of the given
day in that list. You can either use the Docs to locate the
appropriate list method or write a 'for' loop to implement this
function.
'''
# Day to number problem

###################################################
# Student should enter code below

day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def day_to_number(day):
  return day_list.index(day)
###################################################
# Test data

print (day_to_number("Sunday"))
print (day_to_number("Monday"))
print (day_to_number("Tuesday"))
print (day_to_number("Wednesday"))
print (day_to_number("Thursday"))
print (day_to_number("Friday"))
print (day_to_number("Saturday"))

###################################################
# Sample output

#0
#1
#2
#3
#4
#5
#6

