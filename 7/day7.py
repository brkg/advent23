# dict holds dir as keys, and tuples (index of -, dir value) as values
# loop through lines, check index of '-'
# if dir is \, don't calculate value
# otherwise, if dict[dir] is null, init dict[dir] = (currentIndex, 0)
# find index of =, go one after to find value of current line
# pass list of dirs to add as total
# if index of - <= a past dir, remove those dirs from the list of parents
# this should be done recursively?

dict = {}
currentParents = []

def parseLine(line):
  global dict, currentParents
  indexOfDir = line.index('-')
  line = line.strip()
  splitLine = line.split(' ')
  for char in splitLine:
    print(char)
  print(splitLine)

file = open("input.txt", "r")
for line in file:
  parseLine(line)
file.close()
