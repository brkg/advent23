import json
SYM = "symbols"
tuples = {}
seen = {}
sum = 0

# return tuples of (numbers, start/end indices of numbers, indices of symbols)
def parseLine(line):
  dict = {
    SYM: []
  }
  currentNum = ''
  startIndex = 0
  for i, l in enumerate(line):
    if l == '.' and not l.isdigit():
      if currentNum != '':
        dict[startIndex] = int(currentNum)
      startIndex = i
      currentNum = ''
    elif l.isdigit():
      currentNum += l
    else:
      if i != len(line) - 1:
        dict[SYM].append(i)
  return dict

def is_neighbor(row, col, sym_index, val):
  global seen
  xy = str(row) + str(col)
  if xy in seen.keys():
    return False
  val_length = col + len(str(val))
  is_neighbor = (col <= sym_index) and (sym_index <= (col + val_length))
  if is_neighbor:
    seen[xy] = val
  return is_neighbor

def get_neighbors(row, sym_index):
  global tuples, sum 
  sentinel = "-1"
  up = int(row) - 1
  down = int(row)+1
  if up < 0:
    up = sentinel
  if down > len(tuples.keys()):
    down = sentinel
  if len(tuples[row].items()) > 1:
    for key, value in tuples[row].items():
      if key != SYM and is_neighbor(row, key, sym_index, value):
          sum += value
  if up != sentinel:
    for key, value in tuples[up].items():
      if key != SYM and is_neighbor(up, key, sym_index, value):
          sum += value
  if down != sentinel:
    for key, value in tuples[down].items():
      if key != SYM and is_neighbor(down, key, sym_index, value):
          sum += value
  
def getSum():
  global sum
  for rowNum in tuples:
    if len(tuples[rowNum][SYM]) > 0:
      for symbol in tuples[rowNum][SYM]:
        get_neighbors(rowNum, symbol)
  print(sum)
  
def parseFile():
  global tuples
  file = open("input.txt", "r")
  for i, line in enumerate(file):
    tuples[i+1] = parseLine(line)
  file.close()
  getSum()

parseFile()