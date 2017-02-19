'''
Given the list 𝚊 in the template, make a new copy 𝚋 of the list 𝚊
using the function 𝚕𝚒𝚜𝚝. Update the first entry in 𝚋 to be zero.
What happened to the first entry in 𝚊? Explain your answer
(in a comment).
'''

# List reference problem

###################################################
# Student should enter code below

a = [5, 3, 1, -1, -3, 5]
b = list(a)
print (a,b)
b[0]=0
print (a,b)

###################################################
# Explanation
'''
Here we made a new object with the values that 'a' was pointing to.
They are completely unrelated.

'''




