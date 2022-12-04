perElfArray = []
localTotal = 0
currentMax = 0

file = open("input.txt", "r")

for x in file:
  if x == '\n':
    perElfArray.append(localTotal)
    if localTotal > currentMax:
      currentMax = localTotal
    localTotal = 0
  else:
    localTotal += int(x)

perElfArray.append(localTotal)
if localTotal > currentMax:
    currentMax = localTotal

file.close()

print(currentMax)
