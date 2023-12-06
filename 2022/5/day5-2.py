# globals
stacks = []
stackIndices = []
end_of_bracket = False
first = True

def findStacks(splitLine):
  global stacks, first, end_of_bracket, stackIndices
  if first:
    first = False
    stacks = [[] for x in splitLine]
  for i in range(0, len(splitLine)):
    l = splitLine[i]
    l = l.strip()
    if l == '' or l == '[' or l == ']':
      continue
    if l == '1':
      end_of_bracket=True
    if not end_of_bracket:
      stacks[i].append(l)
    else:
      stackIndices.append(i)
      stacks[i] = list(reversed(stacks[i]))

  if end_of_bracket:
    stacks = [stack for stack in stacks if len(stack) > 0]
  return

def parseMoves(line):
  line = line.strip()
  splitLine = line.split(' ')
  if splitLine[0] != 'move':
    return
  # assumes line is 'move x from y to z'
  limit = int(splitLine[1])
  from_index = int(splitLine[3]) - 1
  to_index = int(splitLine[5]) - 1
  to_limit = len(stacks[from_index]) - limit
  substack = stacks[from_index][to_limit::]
  stacks[from_index] = stacks[from_index][0: to_limit]
  for ele in substack:
    stacks[to_index].append(ele)
  return

def parseLine(line):
  global end_of_bracket
  if not end_of_bracket:
    findStacks(line)
  else:
    parseMoves(line)

def main():
  file = open('input.txt', 'r')
  for line in file:
    parseLine(line)
  for stack in stacks:
    print(stack.pop())
  file.close()

main()