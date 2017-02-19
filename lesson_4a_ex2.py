'''
Given the list 𝚊 in the template, make a new reference 𝚋 to 𝚊.
Update the first entry in 𝚋 to be zero. What happened to the
first entry in 𝚊? Explain your answer (in a comment). 
'''

# List reference problem

###################################################
# Student should enter code below

a = [5, 3, 1, -1, -3, 5]
b = a
print (a,b)
b[0]=0
print (a,b)

#lists are mutable.
#lists are objects
#referencing a variable to a list is actually 
#setting a pointer that points to that object 
#in memory
# When we made reference of b to a, we pointed b at the 
#location in memory where that list is stored.
#any change of the pointer b will result in an actual change of that 
#memory allocation so pointer 'a' points to that changed value
#in memory