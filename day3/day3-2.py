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

def parseLines(lines):
  first = dict.fromkeys(lines[0])
  second = dict.fromkeys(lines[1])
  third = dict.fromkeys(lines[2])
  print(first, second, third)
  commonKeys = first.items() & second.items() & third.items()
  for i in commonKeys:
    letter = i[0]
    if letter == '\n':
      continue
    if letter.isupper():
      priorityList.append(prioritiesDict[letter.lower()]+ 26)
    else:
      priorityList.append(prioritiesDict[letter])

makePriorities()
file = open('input.txt', 'r')
groups = []
j = 1
for line in file:
  groups.append(line)
  print(line)
  if j % 3 == 0:
    parseLines(groups)
    groups = []
  j += 1
print(sum(priorityList))
file.close()
