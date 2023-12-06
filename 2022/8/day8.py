visible = 0
depth = 0
arr = []
visited = {}

def parseLine(line):
  global arr, depth, visited
  line = line.strip()
  for i in range(0, len(line)):
    if i >= len(arr):
      arr.append([line[i]])
    arr[i].append(line[i])
  depth += 1

def parseArr(arr):
  global visible
  for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
      if i == 0 or j == 0 or i == len(arr) -1 or j == len(arr[i]) - 1:
        visible += 1
        continue
      

file = open("input.txt", "r")
for line in file:
  parseLine(line)
print(arr)
parseArr(arr)
print(visible)
file.close()
