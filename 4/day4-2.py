def parseLine(line):
  global count
  first = line.split(',')[0].split('-')
  second = line.split(',')[1].split('-')
  a = int(first[0])
  b = int(first[1])+1
  c = int(second[0])
  d = int(second[1])+1
  
  if a >= c:
    for i in range(c, d):
      if i == a or i == b:
        count += 1
        break
  else:
    for i in range(a, b):
      if i == c or i == d:
        count += 1
        break

count = 0
file = open('input.txt', 'r')
for line in file:
  parseLine(line)
print(count)
file.close()