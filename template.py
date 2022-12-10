def parseLine(line):
  print(line)

file = open("input.txt", "r")
for line in file:
  parseLine(line)
file.close()
