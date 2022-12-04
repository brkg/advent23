perElfArray = []
localTotal = 0

file = open("input.txt", "r")
for x in file:
  if x == '\n':
    perElfArray.append(localTotal)
    localTotal = 0
  else:
    localTotal += int(x)

perElfArray.append(localTotal)
perElfArray.sort(reverse=True)

file.close()

print(perElfArray[0],perElfArray[1], perElfArray[2], perElfArray[0]+perElfArray[1]+perElfArray[2])
