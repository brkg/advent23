perElfArray = []
localTotal = 0
currentMax = 0

def findMax():
  global currentMax
  global localTotal
  if localTotal > currentMax:
    currentMax = localTotal

file = open("input.txt", "r")
for x in file:
  if x == '\n':
    perElfArray.append(localTotal)
    findMax()
    localTotal = 0
  else:
    localTotal += int(x)

perElfArray.append(localTotal)
findMax()

file.close()

print(currentMax)
