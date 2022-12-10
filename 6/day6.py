queue = []
count = 0

def is_unique(array):
  return len(set(array)) == len(array)

def parseLine(line):
  global queue, count
  for x in line:
    if len(queue) == 4:
      if is_unique(queue):
        print(count)
        return
    else:
      count += 1
      queue.append(x)
      continue
    queue.pop(0)
    count += 1
    queue.append(x)

file = open("input.txt", "r")
for line in file:
  parseLine(line)
file.close()
