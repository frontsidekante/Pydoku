import copy
import random
import os

numbers = [1,2,3,4,5,6,7,8,9]
random.shuffle(numbers)
### empty list
row = []
row.append(numbers)
print row
### fill list
for index in range(0, 9, 1):
    random.shuffle(numbers)
    row[index] = copy.copy(numbers)
    row.append(numbers)
print row

### row[x][y] -> x is list element, y is element whithin that list
print row[0][0]
#TODO: shuffle until sudokuesqueness is established






