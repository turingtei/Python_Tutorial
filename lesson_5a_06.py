'''
Iteration
  step thru each element of a list and do something to them
'''
def countOddNumbers(numbers):
  count = 0
  for i in numbers:
    if i % 2 == 1:
      count += 1
  return count

def checkIfOddNumbers(numbers):
  '''odd = False   #boolean flag
  for i in numbers:
    if i % 2 == 1:
      odd = True
  return True'''

  #more efficient
  for i in numbers:
    if i % 2 == 1:
      return True
  return False

def removeOddNumbers(numbers):
  remove = []
  for i in numbers:
    if i % 2 == 1:
      remove.append(i)
  for i in remove:
    numbers.pop(numbers.index(i))
  return numbers

def removeOddNumbers2(numbers):
  remove = []
  for i in numbers:
    if i % 2 == 1:
      remove.append(i)
  for i in remove:
    numbers.remove(i)
  return numbers

def removeOddNumbers3(numbers):
  evenNums = []
  for i in numbers:
    if i % 2 == 0:
      evenNums.append(i)
  return evenNums

def removeLastOdd(numbers):
  oddIndex = []
  hasOdd = False
  oddNumber = 0
  for i in range(len(numbers)):
    if numbers[i] % 2 == 1:
      hasOdd = True
      oddIndex.append(i)
  if hasOdd:
    numbers.pop(oddIndex[-1])
  return numbers

def run():
  numbers = [1,7,2,34,8,7,2,5,14,22,93,48,76,15,16,7,19]
  print (numbers)
  #print (countOddNumbers(numbers))
  #print (checkIfOddNumbers(numbers))
  #print (removeOddNumbers(numbers))
  #print (removeOddNumbers2(numbers))
  #print (removeOddNumbers3(numbers))
  #print (removeLastOdd(numbers))
  print (removeLastOdd(numbers))
run()
