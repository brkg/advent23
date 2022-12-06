def parseLine(line):
  global count
  counted = False
  first = line.split(',')[0].split('-')
  second = line.split(',')[1].split('-')
  a = int(first[0])
  b = int(first[1])+1
  c = int(second[0])
  d = int(second[1])+1
  if a >= c:
    for i in range(c, d):
      if i == a or i == b:
        counted = True
  else:
    for i in range(a, b):
      if i == c or i == d:
        counted = True
  if counted:
    count += 1
  # elif first[1] <= second[1] and (first[0] <= second[1] and second[0] >= first[0]):
  #   count += 1  
  # elif second[1] <= first[1] and (second[0] <= first[1] and first[0] >= second[0]):
  #   count += 1

count = 0
file = open('input.txt', 'r')
for line in file:
  parseLine(line)
print(count)
file.close()