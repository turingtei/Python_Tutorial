'''Write a function add_vector(v,w) that takes two 2D vectors v and w 
(represented as lists) and returns a new 2D vector 
(represented as a list) that is the sum of the two vectors. 
Remember that vector addition is performed independently on each
corresponding element of the lists. Hint: returning v + w does not work. 
'''

# Vector addition function

###################################################
# Student should enter code below
def add_vector(v,w):
  added = []
  for i in range(len(v)):
    added.append(v[i] + w[i])
  return added



###################################################
# Test

print (add_vector([4, 3], [0, 0]))
print (add_vector([1, 2], [3, 4]))
print (add_vector([2, 3], [-6, -3]))



###################################################
# Output

#[4, 3]
#[4, 6]
#[-4, 0]

