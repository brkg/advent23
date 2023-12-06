def parseLine(line):
  global count
  first = line.split(',')[0].split('-')
  second = line.split(',')[1].split('-')
  if int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
    count += 1
  elif int(second[0]) >= int(first[0]) and int(second[1]) <= int(first[1]):
    count += 1

count = 0
file = open('input.txt', 'r')
for line in file:
  parseLine(line)
print(count)
file.close()