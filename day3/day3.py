# get list of stuff, read one line at a time
# cut each line in half to get first and second compartments
# find the common letters
# find the priorities, store in list
# sum the priorities

alphabet = 'abcdefghijklmnopqrstuvwxyz'
prioritiesDict = {}
priorityList = []

def makePriorities():
  global alphabet
  global prioritiesDict
  prioritiesDict = dict.fromkeys(alphabet)
  int = 1
  for i in alphabet:
    prioritiesDict[i] = int
    int += 1

def parseLine(line):
  halfwayMark = int(len(line)/2)
  firstHalf = dict.fromkeys(line[0:halfwayMark])
  secondHalf = dict.fromkeys(line[halfwayMark::])
  commonKeys = firstHalf.items() & secondHalf.items()
  for i in commonKeys:
    letter = i[0]
    if letter.isupper():
      priorityList.append(prioritiesDict[letter.lower()]+ 26)
    else:
      priorityList.append(prioritiesDict[letter])

makePriorities()
file = open('input.txt', 'r')
for line in file:
  parseLine(line)
print(sum(priorityList))
file.close()
