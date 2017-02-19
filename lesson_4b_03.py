'''
print (1 is 1)
print (1.0 is 1.0)
print (True is True)
print ('abc' is 'abc')
print ([4,5,6] is [4,5,6])

#tuples

print ((4,5,6) is (4,5,6))
'''
###################################
# Lists (mutable) vs. tuples (immutable)

print ([4, 5, 6])

print ((4, 5, 6))

print (type([4, 5, 6]))

print (type((4, 5, 6)))

a = [4, 5, 6]
a[1] = 100
print (a)

b = (4, 5, 6)
#b[1] = 100
print (b)
